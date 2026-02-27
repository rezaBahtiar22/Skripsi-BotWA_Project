# Implementasi Bot Deteksi Pesan Spam WhatsApp menggunakan SVM

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

Repositori ini berisi kode sumber untuk proyek skripsi berjudul **"Implementasi Bot untuk Deteksi Pesan Spam pada WhatsApp menggunakan Algoritma Support Vector Machine"**. Sistem ini mengintegrasikan bot WhatsApp berbasis JavaScript dengan engine Machine Learning berbasis Python secara real-time.

> **Catatan Peneliti:** Hasil penelitian dan pengembangan sistem ini masih jauh dari kata sempurna. Terdapat berbagai keterbatasan baik dari sisi dataset maupun cakupan fitur, sehingga proyek ini sangat terbuka untuk kritik, saran, dan pengembangan lebih lanjut.

## 📌 Fitur Utama
* **Klasifikasi 3 Kategori:** Sistem mampu membedakan pesan ke dalam kategori **Penipuan**, **Promosi** (keduanya dianggap Spam), dan **Normal**.
* **Peringatan Sistem:** Memberikan notifikasi peringatan otomatis jika pesan yang masuk terindikasi sebagai spam.
* **Logging untuk Dataset:** Setiap pesan yang terdeteksi sebagai spam akan disimpan secara otomatis ke dalam file log sebagai sampel data tambahan untuk proses pelatihan (*training*) di masa depan.
* **Efisiensi Performa:** Model Machine Learning dilatih di Google Colab dan diekspor menjadi file `.pkl`. Hal ini memungkinkan aplikasi berjalan di VS Code tanpa perlu melakukan proses training ulang yang berat.

## 📸 Demo Aplikasi
| Deteksi Pesan Spam | Deteksi Pesan Normal |
| :---: | :---: |
| ![Hasil spam pada WhatsApp](./img/hasil-deteksi-pada-whatsApp.jpeg) | ![Hasil pada terminal](./img/hasil-pada-terminal.png) |

## 🛠️ Persyaratan Sistem (Requirements)
### Machine Learning & Data Science (Python)
Daftar library yang dibutuhkan untuk menjalankan engine klasifikasi:
* **Core ML:** `scikit-learn`, `joblib`
* **Data Handling:** `pandas`, `numpy`
* **Text Preprocessing:** `nltk`, `Sastrawi`
* **Visualization:** `matplotlib`
* **Web API:** `flask`, `flask-ngrok` (opsional untuk deployment)

### Bot WhatsApp (JavaScript)
Daftar dependensi yang digunakan pada Node.js/Bun:
* `whatsapp-web.js`: Integrasi akun WhatsApp.
* `axios`: Menghubungkan bot dengan API Machine Learning Python.
* `qrcode-terminal`: Menampilkan QR code di terminal untuk login.

## 📂 Struktur Proyek
* `APIpy/`: Berisi kode Python, API Flask, dan model `.pkl` hasil training.
* `main/`: Logika utama bot WhatsApp menggunakan JavaScript.
* `logs/`: Tempat penyimpanan sampel pesan spam yang terdeteksi.

## 🚀 Cara Menjalankan
1. **Jalankan API Python:** Masuk ke folder API dan jalankan `app.py` untuk mengaktifkan model SVM.
2. **Jalankan Bot JS:** Buka terminal baru, jalankan bot menggunakan perintah `bun start` atau `node index.js`.
3. **Scan QR Code:** Gunakan fitur tautkan perangkat pada WhatsApp untuk menghubungkan bot.

## 🚀 Pengembangan Mendatang (Future Improvements)
Sesuai dengan saran pada laporan penelitian, sistem ini dapat dikembangkan lebih lanjut melalui:
* **Optimasi Dataset:** Perluasan jumlah data dengan distribusi kelas yang lebih seimbang agar model lebih representatif.
* **Eksperimen Algoritma:** Perbandingan performa SVM dengan algoritma lain seperti Random Forest, Naïve Bayes, hingga Deep Learning (LSTM/Transformer).
* **Pengayaan Fitur:** Implementasi analisis semantik menggunakan Word Embeddings (Word2Vec, FastText, atau BERT).
* **Metrik Evaluasi Lanjutan:** Penambahan analisis ROC-AUC dan *error analysis* untuk identifikasi kelemahan sistem secara spesifik.
* **Feedback Loop:** Penambahan mekanisme umpan balik dari pengguna untuk melatih ulang model agar lebih adaptif.
* **Privasi & Keamanan:** Penerapan enkripsi dan mekanisme anonimisasi data untuk menjaga privasi pesan pengguna.

---
**Dibuat oleh:** Reza Bahtiar Saputra  
**Program Studi:** Teknologi Informasi  
**Universitas Bumigora**