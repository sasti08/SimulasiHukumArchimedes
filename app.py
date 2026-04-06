import streamlit as st
import time
import math
from streamlit_autorefresh import st_autorefresh

# =====================
# SETUP HALAMAN
# =====================
st.set_page_config(page_title="Archimedes", page_icon="🌊", layout="centered")

# =====================
# STYLE AESTHETIC
# =====================
st.markdown("""
<style>
body {
    background: #93c5fd;  /* Biru terang */
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
        Hukum Archimedes menjelaskan bahwa benda yang dicelupkan ke dalam fluida
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
    st.title("🌊 Simulasi Archimedes")

    # Input angka manual
    rho = st.number_input("Massa jenis fluida (kg/m³)", value=1000.0, min_value=0.0, step=10.0)
    volume = st.number_input("Volume benda (m³)", value=1.0, min_value=0.0, step=0.1)
    massa = st.number_input("Massa benda (kg)", value=2.0, min_value=0.0, step=0.1)

    g = 9.8
    Fa = rho * g * volume
    W = massa * g

    # Tentukan kondisi & target posisi balok
    if Fa > W:
        kondisi = "Terapung"
        st.success("🟢 Terapung")
        target = 150
    elif Fa == W:
        kondisi = "Melayang"
        st.info("🟡 Melayang")
        target = 80
    else:
        kondisi = "Tenggelam"
        st.error("🔴 Tenggelam")
        target = 10

    # Info gaya
    st.markdown(f"""
    <div class="card">
    Gaya Apung: <b>{Fa:.2f} N</b> <br>
    Berat Benda: <b>{W:.2f} N</b> <br>
    Kondisi: <b>{kondisi}</b>
    </div>
    """, unsafe_allow_html=True)

    # Autorefresh untuk animasi
    st_autorefresh(interval=50, limit=None, key="refresh_sim")

    # Inisialisasi posisi balok
    if "posisi" not in st.session_state:
        st.session_state.posisi = target

    # Osilasi balok
    t = time.time()
    posisi = st.session_state.posisi
    posisi += (target - posisi) * 0.1
    posisi += 10 * math.sin(t * 3)
    st.session_state.posisi = posisi

    # Render air + balok
    st.markdown(f"""
    <div style="
        height:280px;
        width:300px;
        background:#2563eb;
        border-radius:15px;
        position:relative;
        overflow:hidden;
        margin:auto;
    ">                         
        <!-- Balok coklat -->
        <div style="
            width:60px;
            height:60px;
            background:#8B4513;
            position:absolute;
            left:50%;
            transform:translateX(-50%);
            bottom:{posisi}px;
            border-radius:10px;
            box-shadow:0 10px 20px rgba(0,0,0,0.3);
            transition: bottom 0.1s linear;
        "></div> 
    </div>
    """, unsafe_allow_html=True)

# =====================
# GAME
# =====================
elif menu == "🎮 Game":
    st.title("🎮 Hitung Gaya Apung")

    # Soal contoh
    rho = 1400
    V = 10
    m = 10
    g = 10

    Fa = rho * g * V

    st.markdown(f"""
    <div class="card">
    ρ = {rho} kg/m³ <br>
    V = {V} m³ <br>
    m = {m} kg <br><br>
    <b>Pertanyaan:</b><br>
    Berapa gaya apung benda? (N)
    </div>
    """, unsafe_allow_html=True)

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
