1. Judul
Aplikasi Analisis Topik Pidato Presiden RI Tahun 2014–2024 Menggunakan TF-IDF, LDA, dan BERTopic Berbasis Flask
________________________________________
2. Tujuan
Tujuan dari aplikasi ini adalah untuk:
•	Melakukan analisis topik secara otomatis terhadap teks pidato tahunan Presiden Republik Indonesia tahun 2014–2024.
•	Memberikan visualisasi sederhana berupa daftar kata kunci per topik yang dapat dipahami oleh pengguna awam.
•	Menyediakan perbandingan hasil analisis berdasarkan tiga pendekatan: TF-IDF (Information Retrieval), LDA (Latent Dirichlet Allocation), dan BERTopic (Embedding-Based Topic Modeling).
________________________________________
3. Struktur Proyek
Struktur direktori aplikasi adalah sebagai berikut:
php
CopyEdit
topic_analysis/
│
├── app.py                      # Aplikasi utama Flask
├── utils.py                    # Fungsi pendukung (scraping, preprocessing, analisis)
├── templates/
│   ├── index.html              # Halaman utama (form metode)
│   ├── results.html            # Hasil analisis topik
│   └── topic_detail.html       # Detil kata kunci per topik
│
├── static/                     # (opsional) CSS/JS tambahan jika digunakan
├── requirements.txt            # Daftar dependensi
└── README.md                   # Dokumentasi singkat
________________________________________
4. Teknologi yang Digunakan
•	Python 3.10+
•	Flask – untuk framework web.
•	BeautifulSoup & Requests – untuk web scraping teks pidato.
•	Scikit-learn – untuk TF-IDF dan LDA.
•	BERTopic – untuk analisis topik berbasis embedding.
•	Jinja2 – untuk templating HTML.
•	HTML + CSS (inline) – untuk antarmuka pengguna.
________________________________________
5. Cara Menjalankan
1.	Clone atau unduh repository project.
2.	Install dependencies menggunakan pip:  
pip install -r requirements.txt
3.	Jalankan aplikasi:
python app.py
4.	Buka browser dan akses:
http://127.0.0.1:5000/
________________________________________
6. Sumber Data
Data teks pidato Presiden RI diambil secara web scraping dari beberapa situs resmi dan berita daring, seperti:
•	https://setkab.go.id/pidato-presiden-joko-widodo-pada-pelantikan-presiden-dan-wakil-presiden-republik-indonesia-di-gedung-mpr-senayan-jakarta-20-oktober-2014/
•	https://setkab.go.id/pidato-presiden-republik-indonesia-di-depan-sidang-tahunan-mpr-ri-tahun-2015-jakarta-14-agustus-2015/
•	https://www.antaranews.com/berita/578992/naskah-lengkap-pidato-presiden-di-depan-sidang-tahunan-mpr
•	https://nasional.okezone.com/read/2017/08/16/337/1757203/teks-pidato-kenegaraan-lengkap-yang-disampaikan-presiden-jokowi-di-sidang-tahunan-mpr?page=all
•	https://www.antaranews.com/berita/737723/pidato-lengkap-presiden-joko-widodo-pada-sidang-tahunan-mpr-2018
•	https://jeo.kompas.com/naskah-lengkap-pidato-tahunan-2019-presiden-jokowi
•	https://jeo.kompas.com/naskah-lengkap-pidato-kenegaraan-presiden-jokowi-2020
•	https://pa-soreang.go.id/ini-isi-pidato-presiden-jokowi-dalam-sidang-istimewa-laporan-tahunan-mahkamah-agung-ri-2020-17-02-21/
•	https://jeo.kompas.com/naskah-lengkap-pidato-kenegaraan-presiden-joko-widodo-tahun-2022
•	https://setkab.go.id/pidato-presiden-ri-pada-sidang-tahunan-mpr-ri-dan-sidang-bersama-dpr-ri-dan-dpd-ri-dalam-rangka-hut-ke-78-proklamasi-kemerdekaan-ri-di-gedung-nusantara-mpr-dpr-dpd-ri-senayan-provinsi-dki-jakarta/
•	https://setkab.go.id/pidato-kenegaraan-pada-sidang-tahunan-mpr-ri-dan-sidang-bersama-dpr-dan-dpd-ri-dalam-rangka-hut-ke-79-proklamasi-kemerdekaan-ri-di-gedung-nusantara-i-kompleks-perkantoran-mpr-dpr-dpd-ri-senayan-pro/
________________________________________
7. Saran
•	Tambahkan visualisasi seperti grafik distribusi topik per tahun.
•	Gunakan penyimpanan cache atau database untuk menyimpan hasil scraping agar tidak mengulang proses setiap kali.
•	Perlu ditambahkan validasi scraping jika struktur halaman berubah.
•	Implementasikan upload dokumen pidato oleh pengguna secara manual.
•	Tambahkan fitur download hasil analisis dalam format CSV atau PDF.

