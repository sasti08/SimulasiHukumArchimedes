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

    rho_benda = st.number_input("Massa jenis benda", 1.0, 2000.0, 500.0)
    rho_fluida = st.number_input("Massa jenis fluida", 1.0, 2000.0, 1000.0)

    # STATE
    if "y" not in st.session_state:
        st.session_state.y = 120
    if "status" not in st.session_state:
        st.session_state.status = ""

    start = st.button("▶️ Simulasikan")

    if start:
        # reset posisi
        st.session_state.y = 120

        # tentukan kondisi
        if rho_benda < rho_fluida:
            st.session_state.status = "Terapung 🟢"
        elif rho_benda == rho_fluida:
            st.session_state.status = "Melayang 🟡"
        else:
            st.session_state.status = "Tenggelam 🔴"

    st.write(f"Status: **{st.session_state.status}**")

    placeholder = st.empty()

    # =====================
    # ANIMASI
    # =====================
    for _ in range(80):
        y = st.session_state.y
        status = st.session_state.status

        # GERAKAN
        if "Terapung" in status and y > 60:
            y -= 2
        elif "Tenggelam" in status and y < 200:
            y += 2
        elif "Melayang" in status:
            if y < 120:
                y += 1
            elif y > 120:
                y -= 1

        st.session_state.y = y

        placeholder.markdown(f"""
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

            <!-- GARIS PERMUKAAN -->
            <div style="
                position:absolute;
                bottom:150px;
                width:100%;
                height:2px;
                background:white;
            "></div>

            <!-- BALOK -->
            <div style="
                width:60px;
                height:60px;
                background:#8B4513;
                position:absolute;
                left:50%;
                transform:translateX(-50%);
                bottom:{y}px;
                border-radius:5px;
                box-shadow:0 10px 20px rgba(0,0,0,0.3);
            "></div>

        </div>
        """, unsafe_allow_html=True)

        time.sleep(0.05)

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
