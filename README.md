# Aplikasi Analisis Topik Pidato Presiden RI Tahun 2014–2024 Menggunakan TF-IDF, LDA, dan BERTopic Berbasis Flask

## Tujuan
Tujuan dari aplikasi ini adalah untuk:
- Melakukan analisis topik secara otomatis terhadap teks pidato tahunan Presiden Republik Indonesia tahun 2014–2024.
- Memberikan visualisasi sederhana berupa daftar kata kunci per topik yang dapat dipahami oleh pengguna awam.
- Menyediakan perbandingan hasil analisis berdasarkan tiga pendekatan: TF-IDF (Information Retrieval), LDA (Latent Dirichlet Allocation), dan BERTopic (Embedding-Based Topic Modeling).

---

## Struktur Proyek
Struktur direktori aplikasi adalah sebagai berikut:

topic_analysis/
│
├── app.py # Aplikasi utama Flask
├── utils.py # Fungsi pendukung (scraping, preprocessing, analisis)
├── templates/
│ ├── index.html # Halaman utama (form metode)
│ ├── results.html # Hasil analisis topik
│ └── topic_detail.html # Detil kata kunci per topik
│
├── static/ # (opsional) CSS/JS tambahan jika digunakan
├── requirements.txt # Daftar dependensi
└── README.md # Dokumentasi singkat


---

## Teknologi yang Digunakan
- **Python 3.10+**
- **Flask** – untuk framework web.
- **BeautifulSoup & Requests** – untuk web scraping teks pidato.
- **Scikit-learn** – untuk TF-IDF dan LDA.
- **BERTopic** – untuk analisis topik berbasis embedding.
- **Jinja2** – untuk templating HTML.
- **HTML + CSS (inline)** – untuk antarmuka pengguna.

---

## Cara Menjalankan

1. **Clone atau unduh repository project**:
    ```bash
    git clone https://github.com/Mr-XDev/Tugas-UTS-NLP.git
    ```

2. **Install dependencies menggunakan pip**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Jalankan aplikasi**:
    ```bash
    python app.py
    ```

4. **Buka browser dan akses aplikasi**:
    ```
    http://127.0.0.1:5000/
    ```
![image](https://github.com/user-attachments/assets/1adfb345-ecf1-430b-a3a6-7b975ebeecb6)

![image](https://github.com/user-attachments/assets/cd2c7fd7-d63a-456b-a729-ba893b7c04c2)

![image](https://github.com/user-attachments/assets/9c227f09-9603-4738-bad7-e8c4c08a5c4b)


---

## Sumber Data
Data teks pidato Presiden RI diambil secara web scraping dari beberapa situs resmi dan berita daring, seperti:

1. [Pidato Presiden 2014](https://setkab.go.id/pidato-presiden-joko-widodo-pada-pelantikan-presiden-dan-wakil-presiden-republik-indonesia-di-gedung-mpr-senayan-jakarta-20-oktober-2014/)
2. [Pidato Presiden 2015](https://setkab.go.id/pidato-presiden-republik-indonesia-di-depan-sidang-tahunan-mpr-ri-tahun-2015-jakarta-14-agustus-2015/)
3. [Pidato Presiden 2016](https://www.antaranews.com/berita/578992/naskah-lengkap-pidato-presiden-di-depan-sidang-tahunan-mpr)
4. [Pidato Presiden 2017](https://nasional.okezone.com/read/2017/08/16/337/1757203/teks-pidato-kenegaraan-lengkap-yang-disampaikan-presiden-jokowi-di-sidang-tahunan-mpr?page=all)
5. [Pidato Presiden 2018](https://www.antaranews.com/berita/737723/pidato-lengkap-presiden-joko-widodo-pada-sidang-tahunan-mpr-2018)
6. [Pidato Presiden 2019](https://jeo.kompas.com/naskah-lengkap-pidato-tahunan-2019-presiden-jokowi)
7. [Pidato Presiden 2020](https://jeo.kompas.com/naskah-lengkap-pidato-kenegaraan-presiden-jokowi-2020)
8. [Pidato Presiden 2021](https://pa-soreang.go.id/ini-isi-pidato-presiden-jokowi-dalam-sidang-istimewa-laporan-tahunan-mahkamah-agung-ri-2020-17-02-21/)
9. [Pidato Presiden 2022](https://jeo.kompas.com/naskah-lengkap-pidato-kenegaraan-presiden-jokowido-tahun-2022)
10. [Pidato Presiden 2023](https://setkab.go.id/pidato-presiden-ri-pada-sidang-tahunan-mpr-ri-dan-sidang-bersama-dpr-ri-dan-dpd-ri-dalam-rangka-hut-ke-78-proklamasi-kemerdekaan-ri-di-gedung-nusantara-mpr-dpr-dpd-ri-senayan-provinsi-dki-jakarta/)
11. [Pidato Presiden 2024](https://setkab.go.id/pidato-kenegaraan-pada-sidang-tahunan-mpr-ri-dan-sidang-bersama-dpr-dan-dpd-ri-dalam-rangka-hut-ke-79-proklamasi-kemerdekaan-ri-di-gedung-nusantara-i-kompleks-perkantoran-mpr-dpr-dpd-ri-senayan-pro/)

---

## Saran
- Tambahkan visualisasi seperti grafik distribusi topik per tahun.
- Gunakan penyimpanan cache atau database untuk menyimpan hasil scraping agar tidak mengulang proses setiap kali.
- Perlu ditambahkan validasi scraping jika struktur halaman berubah.
- Implementasikan upload dokumen pidato oleh pengguna secara manual.
- Tambahkan fitur download hasil analisis dalam format CSV atau PDF.
