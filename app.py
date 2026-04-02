import os
import streamlit as st
import pandas as pd
import joblib

# Setup konfigurasi halaman
st.set_page_config(page_title="Prediksi Status Siswa", layout="wide", page_icon="🎓")

# Judul Utama
st.title("🎓 Prototype Prediksi Status Mahasiswa")
st.write("Aplikasi ini menggunakan model Machine Learning (Random Forest) untuk memprediksi apakah seorang mahasiswa berpotensi **Dropout**, tetap **Enrolled**, atau **Graduate**.")
st.markdown("---")

# 1. Load Data, Model, dan Scaler
@st.cache_data
def load_data():
    # Menggunakan OS path agar tidak terjadi error FileNotFoundError
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data.csv')
    df = pd.read_csv(file_path, sep=';')
    return df

@st.cache_resource
def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    rf_path = os.path.join(current_dir, 'model', 'rf_model.joblib')
    scaler_path = os.path.join(current_dir, 'model', 'scaler.joblib')
    
    rf_model = joblib.load(rf_path)
    scaler = joblib.load(scaler_path)
    return rf_model, scaler

# Coba Load Data
try:
    df = load_data()
    X = df.drop(columns=['Status'])
    data_loaded = True
except FileNotFoundError:
    st.error("⚠️ File 'data.csv' tidak ditemukan! Pastikan file berada di folder yang sama dengan app.py.")
    data_loaded = False

# Coba Load Model
try:
    rf_model, scaler = load_model()
    model_loaded = True
except FileNotFoundError:
    st.error("⚠️ Model atau Scaler tidak ditemukan! Pastikan file 'rf_model.joblib' dan 'scaler.joblib' ada di dalam folder 'model'.")
    model_loaded = False

# ==========================================
# KAMUS PENJELASAN KOLOM UNTUK TOOLTIP (i)
# ==========================================
penjelasan_kolom = {
    "Marital_status": "Status pernikahan mahasiswa (Contoh: 1 = Belum Menikah, 2 = Menikah, dsb).",
    "Course": "Kode program studi atau jurusan yang diambil oleh mahasiswa.",
    "Tuition_fees_up_to_date": "Status pembayaran SPP (1 = Lunas/Tepat waktu, 0 = Menunggak).",
    "Scholarship_holder": "Apakah mahasiswa menerima beasiswa? (1 = Ya, 0 = Tidak).",
    "Age_at_enrollment": "Usia mahasiswa saat pertama kali mendaftar ke institusi.",
    "Curricular_units_1st_sem_grade": "Rata-rata nilai mahasiswa pada evaluasi semester 1.",
    "Curricular_units_2nd_sem_grade": "Rata-rata nilai mahasiswa pada evaluasi semester 2.",
    "Debtor": "Apakah mahasiswa memiliki hutang ke institusi? (1 = Ya, 0 = Tidak).",
    "Gender": "Jenis kelamin mahasiswa (1 = Laki-laki, 0 = Perempuan).",
    "Inflation_rate": "Tingkat inflasi ekonomi pada saat mahasiswa tersebut mendaftar.",
    "GDP": "Produk Domestik Bruto (GDP) nasional saat pendaftaran."
}

# 2. Sidebar untuk Input Pengguna
if data_loaded:
    st.sidebar.header("📝 Input Data Mahasiswa")
    st.sidebar.write("Ubah nilai di bawah ini untuk melihat hasil prediksi.")

    input_data = {}

    for col in X.columns:
        # Ambil penjelasan dari kamus. Jika kolom tidak ada di kamus, gunakan teks default.
        tooltip_text = penjelasan_kolom.get(col, f"Masukkan data untuk metrik {col}")

        if len(X[col].unique()) <= 10:
            input_data[col] = st.sidebar.selectbox(
                f"{col}", 
                options=sorted(X[col].unique()), 
                index=0,
                help=tooltip_text  # <-- INI ADALAH PARAMETER UNTUK MEMUNCULKAN TANDA (i)
            )
        else:
            min_val = float(X[col].min())
            max_val = float(X[col].max())
            mean_val = float(X[col].mean())
            input_data[col] = st.sidebar.slider(
                f"{col}", 
                min_value=min_val, 
                max_value=max_val, 
                value=mean_val,
                help=tooltip_text  # <-- INI ADALAH PARAMETER UNTUK MEMUNCULKAN TANDA (i)
            )

# 3. Proses Prediksi
if model_loaded and data_loaded:
    st.subheader("Data yang dimasukkan:")
    input_df = pd.DataFrame([input_data])
    st.dataframe(input_df)
    
    st.markdown("---")
    
    if st.button("🔍 Prediksi Status Mahasiswa", type="primary"):
        with st.spinner("Sedang memproses..."):
            input_scaled = scaler.transform(input_df)
            prediction = rf_model.predict(input_scaled)
            
            st.subheader("🎯 Hasil Prediksi:")
            if prediction[0] == 'Dropout':
                st.error(f"⚠️ Peringatan: Mahasiswa ini diprediksi akan **{prediction[0]}**.")
                st.write("Saran: Segera jadwalkan konseling akademik atau periksa status finansialnya.")
            elif prediction[0] == 'Graduate':
                st.success(f"🎉 Bagus: Mahasiswa ini diprediksi akan **{prediction[0]}**.")
                st.write("Saran: Pertahankan performa akademik saat ini.")
            else:
                st.info(f"🔄 Status: Mahasiswa ini diprediksi tetap **{prediction[0]}**.")
                st.write("Saran: Lakukan pemantauan rutin pada semester berikutnya.")