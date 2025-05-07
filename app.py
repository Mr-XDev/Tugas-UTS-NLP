from flask import Flask, render_template, request, redirect, url_for, session
import os
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import nltk
from utils import scrape_speech, analyze_tfidf, analyze_lda, analyze_bertopic
import Sastrawi


# Pastikan stopwords sudah diunduh
nltk.download('stopwords')
from utils import (
    scrape_speech,
    preprocess_for_tfidf,
    preprocess_for_lda,
    preprocess_for_bertopic,
    analyze_tfidf,
    analyze_lda,
    analyze_bertopic,
)

app = Flask(__name__)
app.secret_key = os.urandom(24)

# URL referensi pidato
urls = [
    "https://setkab.go.id/pidato-presiden-joko-widodo-pada-pelantikan-presiden-dan-wakil-presiden-republik-indonesia-di-gedung-mpr-senayan-jakarta-20-oktober-2014/",
    "https://setkab.go.id/pidato-presiden-republik-indonesia-di-depan-sidang-tahunan-mpr-ri-tahun-2015-jakarta-14-agustus-2015/",
    "https://www.antaranews.com/berita/578992/naskah-lengkap-pidato-presiden-di-depan-sidang-tahunan-mpr",
    "https://nasional.okezone.com/read/2017/08/16/337/1757203/teks-pidato-kenegaraan-lengkap-yang-disampaikan-presiden-jokowi-di-sidang-tahunan-mpr?page=all",
    "https://www.antaranews.com/berita/737723/pidato-lengkap-presiden-joko-widodo-pada-sidang-tahunan-mpr-2018",
    "https://jeo.kompas.com/naskah-lengkap-pidato-tahunan-2019-presiden-jokowi",
    "https://jeo.kompas.com/naskah-lengkap-pidato-kenegaraan-presiden-jokowi-2020",
    "https://pa-soreang.go.id/ini-isi-pidato-presiden-jokowi-dalam-sidang-istimewa-laporan-tahunan-mahkamah-agung-ri-2020-17-02-21/",
    "https://jeo.kompas.com/naskah-lengkap-pidato-kenegaraan-presiden-joko-widodo-tahun-2022",
    "https://setkab.go.id/pidato-presiden-ri-pada-sidang-tahunan-mpr-ri-dan-sidang-bersama-dpr-ri-dan-dpd-ri-dalam-rangka-hut-ke-78-proklamasi-kemerdekaan-ri-di-gedung-nusantara-mpr-dpr-dpd-ri-senayan-provinsi-dki-jakarta/",
    "https://setkab.go.id/pidato-kenegaraan-pada-sidang-tahunan-mpr-ri-dan-sidang-bersama-dpr-dan-dpd-ri-dalam-rangka-hut-ke-79-proklamasi-kemerdekaan-ri-di-gedung-nusantara-i-kompleks-perkantoran-mpr-dpr-dpd-ri-senayan-pro/"
]

# Fungsi preprocessing teks
def preprocess_text(text):
    # Convert ke huruf kecil
    text = text.lower()
    
    # Hapus angka dan tanda baca
    text = ''.join([char for char in text if char not in string.punctuation and not char.isdigit()])
    
    # Tokenisasi kata-kata
    words = text.split()
    
    # Menghilangkan stopwords
    stop_words = set(stopwords.words('indonesian'))
    words = [word for word in words if word not in stop_words]
    
    # Stemming (atau bisa menggunakan lemmatization jika diperlukan)
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    # Gabungkan kembali kata-kata yang sudah diproses menjadi teks
    return ' '.join(words)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    method = request.form.get('method')
    
    # Scrape dan preprocess dokumen
    raw_documents = [scrape_speech(url) for url in urls]  # Memastikan raw_documents selalu ada
    documents = [preprocess_text(doc) for doc in raw_documents]  # Preprocess raw_documents

    vectorizer = None
    topic_info = []

    if method == 'tfidf':
        X, vectorizer = analyze_tfidf(documents)
        top_indices = np.argsort(X.toarray(), axis=1)[:, -5:]
        feature_names = vectorizer.get_feature_names_out()

        for idx, doc_terms in enumerate(top_indices):
            words_scores = [(feature_names[i], X[idx, i]) for i in doc_terms]
            words_scores.sort(key=lambda x: -x[1])  # urutkan dari skor tertinggi
            topic_info.append({"topic": idx, "words": words_scores})

    elif method == 'lda':
        lda, vectorizer = analyze_lda(documents)
        topics = lda.components_
        top_indices = np.argsort(topics, axis=1)[:, -5:]
        feature_names = vectorizer.get_feature_names_out()

        for idx, topic_terms in enumerate(top_indices):
            words_scores = [(feature_names[i], topics[idx, i]) for i in topic_terms]
            words_scores.sort(key=lambda x: -x[1])
            topic_info.append({"topic": idx, "words": words_scores})

    elif method == 'bertopic':
        # Proses khusus untuk BERTopic
        documents = [preprocess_for_bertopic(doc) for doc in raw_documents]
        topic_model, topics = analyze_bertopic(documents)
        unique_topics = sorted(set(topics))
        top_terms = [topic_model.get_topic(topic)[:5] for topic in unique_topics]

        for idx, topic in enumerate(top_terms):
            topic_info.append({"topic": idx, "words": topic})  # topic = list of (word, score)

    else:
        return "Invalid method", 400

    # Simpan ke session
    session['topic_info'] = topic_info
    session['method'] = method

    return redirect(url_for('results'))  # ← baris ini HARUS berada di dalam fungsi analyze()

@app.route('/results')
def results():
    topics = session.get('topic_info', [])
    method = session.get('method', '')
    return render_template('results.html', topics=topics, method=method)

@app.route('/topic/<int:topic_id>')
def topic_detail(topic_id):
    topics = session.get('topic_info', [])

    method = session.get('method', '')

    if topic_id < 0 or topic_id >= len(topics):
        return redirect(url_for('results'))

    topic = topics[topic_id]
    return render_template('topic_detail.html',
                           topic_id=topic_id,
                           method=method,
                           words=topic['words'])  # <-- ini yang penting



    if topic_id < 0 or topic_id >= len(topics):
        return redirect(url_for('results'))
    topic = topics[topic_id]
    return render_template('topic_detail.html', topic_id=topic_id, words=topic['words'])

if __name__ == '__main__':
    app.run(debug=True)
