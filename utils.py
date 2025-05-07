import requests
from bs4 import BeautifulSoup
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

# Scraping
def scrape_speech(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Ambil semua <p>
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    except Exception as e:
        return f"Error scraping: {str(e)}"

# Preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Hapus angka
    text = text.translate(str.maketrans('', '', string.punctuation))  # Hapus tanda baca
    text = re.sub(r'\s+', ' ', text)  # Hapus spasi ganda
    return text.strip()

# TF-IDF
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from bertopic import BERTopic

from sklearn.feature_extraction.text import CountVectorizer
import traceback

# === Scraping ===
def scrape_speech(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all(['p', 'div'])
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    except:
        return ""

# === Preprocessing ===
factory = StopWordRemoverFactory()
stop_remover = factory.create_stop_word_remover()
stemmer = StemmerFactory().create_stemmer()

def basic_cleaning(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_for_tfidf(text):
    text = basic_cleaning(text)
    text = stop_remover.remove(text)
    text = stemmer.stem(text)
    return text

def preprocess_for_lda(text):
    text = basic_cleaning(text)
    text = stop_remover.remove(text)
    text = stemmer.stem(text)
    return text

def preprocess_for_bertopic(text):
    text = basic_cleaning(text)
    return text

# === TF-IDF ===
def analyze_tfidf(documents):
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(documents)
    return X, vectorizer

# LDA
def analyze_lda(documents, num_topics=5):
    vectorizer = CountVectorizer(max_features=1000, stop_words='english')

# === LDA ===
def analyze_lda(documents, num_topics=5):
    vectorizer = CountVectorizer(max_features=1000)
    X = vectorizer.fit_transform(documents)
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(X)
    return lda, vectorizer

# BERTopic
def analyze_bertopic(documents):
    topic_model = BERTopic(language="indonesian")
    topics, _ = topic_model.fit_transform(documents)
    return topic_model, topics

# === BERTopic ===
def analyze_bertopic(documents):
    try:
        topic_model = BERTopic()
        topics, _ = topic_model.fit_transform(documents)
        return topic_model, topics
    except Exception as e:
        print("BERTopic error:", e)
        traceback.print_exc()
        return None, []
