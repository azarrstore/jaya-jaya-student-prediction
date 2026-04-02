# 🎓 Jaya Jaya Institut - Student Performance Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jaya-jaya-student-prediction.streamlit.app/)

## 📌 Deskripsi Proyek
Aplikasi berbasis web interaktif ini dikembangkan menggunakan **Streamlit** dan **Machine Learning (Random Forest)** untuk memprediksi performa dan status akhir mahasiswa di Jaya Jaya Institut. 

Tujuan utama dari aplikasi ini adalah untuk melakukan **deteksi dini** terhadap mahasiswa yang memiliki risiko tinggi untuk *dropout* (putus kuliah), sehingga pihak institusi dapat segera memberikan intervensi berupa bimbingan akademik atau bantuan finansial.

Proyek ini merupakan Submission Akhir untuk kelas **"Menyelesaikan Permasalahan Perusahaan Edutech"** di Dicoding.

## 🚀 Fitur Utama
- **Prediksi Real-time:** Memasukkan data demografi, akademik, dan ekonomi mahasiswa untuk mendapatkan prediksi status akhir (*Dropout*, *Enrolled*, atau *Graduate*).
- **Sistem Rekomendasi:** Memberikan saran tindakan (*action items*) otomatis berdasarkan hasil prediksi model.
- **UI/UX Interaktif:** Dilengkapi dengan *tooltip* informasi untuk memudahkan pengguna awam memahami setiap metrik input.

## 🛠️ Teknologi yang Digunakan
- **Bahasa Pemrograman:** Python 3.11
- **Web Framework:** Streamlit
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)
- **Data Manipulation:** Pandas, NumPy
- **Deployment:** Streamlit Community Cloud

## 📂 Struktur Repositori
```text
├── model/
│   ├── rf_model.joblib   # Model Machine Learning yang sudah dilatih
│   └── scaler.joblib     # Scaler untuk standardisasi data input
├── app.py                # Kode sumber utama aplikasi Streamlit
├── data.csv              # Dataset referensi untuk batasan input
├── requirements.txt      # Daftar dependensi library Python
└── README.md             # Dokumentasi proyek
````

## 💻 Cara Menjalankan Aplikasi Secara Lokal

Jika Anda ingin menjalankan aplikasi ini di komputer/laptop Anda sendiri, ikuti langkah-langkah berikut:

1.  **Clone repositori ini:**

    ```bash
    git clone https://github.com/azarrstore/jaya-jaya-student-prediction.git
    cd jaya-jaya-student-prediction
    ```

2.  **Buat Virtual Environment (Opsional tapi disarankan):**

    ```bash
    python -m venv env
    source env/bin/activate  # Untuk Mac/Linux
    env\Scripts\activate     # Untuk Windows
    ```

3.  **Install semua dependensi:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan aplikasi Streamlit:**

    ```bash
    streamlit run app.py
    ```

## 📊 Dataset

Dataset yang digunakan dalam proyek ini mencakup informasi mahasiswa pada saat pendaftaran (jalur akademik, demografi, faktor sosial-ekonomi) dan performa akademik pada akhir semester 1 dan 2.

## 👤 Penulis

**Erlangga Azhar**