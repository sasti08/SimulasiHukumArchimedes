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
    st.title("🌊 Simulasi Archimedes")

    rho = st.slider("Massa jenis fluida (kg/m³)", 500, 1500, 1000)
    volume = st.slider("Volume (m³)", 0.1, 5.0, 1.0)
    massa = st.slider("Massa benda (kg)", 0.1, 10.0, 2.0)

    g = 9.8
    Fa = rho * g * volume
    W = massa * g

    st.markdown(f"""
    <div class="card">
    Gaya Apung: <b>{Fa:.2f} N</b> <br>
    Berat Benda: <b>{W:.2f} N</b>
    </div>
    """, unsafe_allow_html=True)

    # =====================
    # STATE START
    # =====================
    if "start_simulasi" not in st.session_state:
        st.session_state.start_simulasi = False

    if st.button("▶️ Start Simulasi"):
        st.session_state.start_simulasi = True

    # Tentukan target posisi
    if Fa > W:
        target = 180
    elif Fa == W:
        target = 90
    else:
        target = 20

    if "posisi" not in st.session_state:
        st.session_state.posisi = 20

    placeholder = st.empty()

    # =====================
    # ANIMASI
    # =====================
    if st.session_state.start_simulasi:
        for _ in range(60):
            t = time.time()

            posisi = st.session_state.posisi
            posisi += (target - posisi) * 0.15

            # osilasi kecil
            if abs(target - posisi) < 5:
                posisi += 5 * math.sin(t * 3)

            st.session_state.posisi = posisi

            # Label dinamis
            if posisi > 150:
                label = "🟢 Terapung"
            elif posisi > 70:
                label = "🟡 Melayang"
            else:
                label = "🔴 Tenggelam"

            placeholder.markdown(f"""
<div style="
    height:300px;
    background:#e0f2fe;
    border-radius:15px;
    position:relative;
    overflow:hidden;
">

    <div style="
        width:100%;
        height:150px;
        background:#2563eb;
        position:absolute;
        bottom:0;
    "></div>

    <div style="
        position:absolute;
        bottom:150px;
        width:100%;
        height:3px;
        background:white;
    "></div>

    <div style="
        position:absolute;
        top:10px;
        left:50%;
        transform:translateX(-50%);
        font-weight:bold;
        font-size:18px;
        color:black;
    ">
        {label}
    </div>

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
