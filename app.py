import streamlit as st
import time
import math

st.set_page_config(page_title="Archimedes", page_icon="🌊", layout="centered")

# =====================
# STYLE (BIAR AESTHETIC)
# =====================
st.markdown("""
<style>
body {
    background: #93c5fd;  /* Warna biru terang */
}
.block-container {
    padding-top: 2rem;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =====================
# NAVBAR
# =====================
menu = st.sidebar.radio("Menu", ["🏠 Home", "🌊 Simulasi", "🎮 Game", "📝 Latihan"])

# =====================
# HOME
# =====================
if menu == "🏠 Home":
    st.title("🌊 Hukum Archimedes")
    st.markdown("""
    <div class="card">
         <h3>📖 Pengertian</h3>
    Hukum Archimedes adalah hukum yang menjelaskan bahwa suatu benda yang dicelupkan ke dalam fluida
    akan mengalami gaya ke atas yang disebut gaya apung.
         <br><br>
         <h3>📜 Bunyi Hukum Archimedes</h3>
    "Suatu benda yang dicelupkan sebagian atau seluruhnya ke dalam fluida akan mengalami gaya ke atas
    sebesar berat fluida yang dipindahkannya."
         <br><br>
         <h3>📘 Rumus</h3>
    Fa = ρ × g × V <br><br>
         <b>Keterangan:</b><br>
    ρ = massa jenis fluida <br>
    g = percepatan gravitasi <br>
    V = volume benda tercelup <br><br>
         <b>Konsep:</b><br>
    🟢 Fa > W → Terapung <br>
    🟡 Fa = W → Melayang <br>
    🔴 Fa < W → Tenggelam
    </div>
    """, unsafe_allow_html=True)

# =====================
# SIMULASI
# =====================
elif menu == "🌊 Simulasi":
    st.title("🌊 Simulasi Sederhana Archimedes")

    st.write("Masukkan nilai:")

    # INPUT MANUAL DARI 0
    massa_benda = st.number_input("Massa benda", 0.0, 10000.0, 0.0)
    massa_jenis_air = st.number_input("Massa jenis air", 0.0, 10000.0, 0.0)

    Fa = st.number_input("Gaya apung (Fa)", 0.0, 10000.0, 0.0)
    W = st.number_input("Berat benda (W)", 0.0, 10000.0, 0.0)

    # KONDISI
    kondisi = "-"
    posisi = 20  # default bawah

    if Fa == W and Fa != 0:
        kondisi = "🟡 Melayang"
        posisi = 100
    elif massa_benda < massa_jenis_air and massa_benda != 0:
        kondisi = "🟢 Terapung"
        posisi = 180
    elif massa_benda > massa_jenis_air:
        kondisi = "🔴 Tenggelam"
        posisi = 20

    st.write(f"**Kondisi: {kondisi}**")

    # VISUAL
    st.markdown(f"""
    <div style="
        height:300px;
        background:#e0f2fe;
        border-radius:15px;
        position:relative;
        overflow:hidden;
    ">

        <!-- AIR SETENGAH -->
        <div style="
            position:absolute;
            bottom:0;
            width:100%;
            height:150px;
            background:#2563eb;
        "></div>

        <!-- GARIS AIR -->
        <div style="
            position:absolute;
            bottom:150px;
            width:100%;
            height:2px;
            background:white;
        "></div>

        <!-- BALOK COKLAT -->
        <div style="
            width:60px;
            height:60px;
            background:#8B4513;
            position:absolute;
            left:50%;
            transform:translateX(-50%);
            bottom:{posisi}px;
            border-radius:5px;
            box-shadow:0 10px 20px rgba(0,0,0,0.3);
        "></div>

    </div>
    """, unsafe_allow_html=True)

# =====================
# GAME
# =====================
elif menu == "🎮 Game":
    st.title("🎮 Hitung Gaya Apung")

    # data soal
    rho = 1400
    V = 10
    m = 10
    g = 10

    Fa = rho * g * V  # jawaban benar

    st.markdown(f"""
    <div class="card">
    ρ = {rho} kg/m³ <br>
    V = {V} m³ <br>
    m = {m} kg <br><br>
     <b>Pertanyaan:</b><br>
    Berapa gaya apung benda? (N)
    </div>
    """, unsafe_allow_html=True)

    # pilihan jawaban tetap dengan satuan N
    pilihan = [f"{Fa} N", f"{Fa + 2000} N", f"{Fa - 2000} N"]

    jawaban_user = st.radio("Pilih jawaban:", pilihan)

    if st.button("Cek Jawaban"):
        if jawaban_user == f"{Fa} N":
            st.success("✅ Benar! 🎉")
        else:
            st.error(f"❌ Salah! Jawaban yang benar: {Fa} N")

# =====================
# LATIHAN
# =====================
elif menu == "📝 Latihan":
    st.title("📝 Latihan Soal")

    soal = [
        {"q": "Fa > W maka?", "opsi": ["Tenggelam", "Terapung", "Hilang"], "jawab": "Terapung"},
        {"q": "Fa = W maka?", "opsi": ["Melayang", "Terapung", "Jatuh"], "jawab": "Melayang"},
        {"q": "Fa < W maka?", "opsi": ["Terapung", "Tenggelam", "Terbang"], "jawab": "Tenggelam"},
    ]

    skor = 0

    for i, s in enumerate(soal):
        jawab = st.radio(s["q"], s["opsi"], key=i)
        if jawab == s["jawab"]:
            skor += 1

    if st.button("Lihat Skor"):
        st.success(f"Skor kamu: {skor}/{len(soal)}")
