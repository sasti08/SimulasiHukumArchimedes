import streamlit as st
import time
import random

st.set_page_config(page_title="Archimedes", page_icon="🌊", layout="centered")

# =====================
# STYLE (BIAR AESTHETIC)
# =====================
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #00bfff, #87cefa);  /* gradient biru laut aesthetic */
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
# SIMULASI PRO
# =====================
elif menu == "🌊 Simulasi":
    st.title("🌊 Simulasi Archimedes")

    rho = st.slider("Massa jenis fluida", 500, 1500, 1000)
    volume = st.slider("Volume", 0.1, 5.0, 1.0)
    massa = st.slider("Massa", 0.1, 10.0, 2.0)

    g = 9.8
    Fa = rho * g * volume
    W = massa * g

    st.markdown(f"""
    <div class="card">
    Gaya Apung: <b>{Fa:.2f}</b> <br>
    Berat Benda: <b>{W:.2f}</b>
    </div>
    """, unsafe_allow_html=True)

    if Fa > W:
        kondisi = "terapung"
        st.success("🟢 Terapung")
    elif Fa == W:
        kondisi = "melayang"
        st.info("🟡 Melayang")
    else:
        kondisi = "tenggelam"
        st.error("🔴 Tenggelam")

    # ===== SIMULASI GACOR =====
    st.subheader("🌊 Simulasi Gerakan")

    col1, col2 = st.columns(2)
    with col1:
        start = st.button("▶️ Start")
    with col2:
        speed = st.slider("Speed", 0.01, 0.2, 0.05)

    if kondisi == "terapung":
        target = 150
    elif kondisi == "melayang":
        target = 80
    else:
        target = 10

    if "posisi" not in st.session_state:
        st.session_state.posisi = 20

    placeholder = st.empty()

    if start:
        for i in range(60):
            st.session_state.posisi += (target - st.session_state.posisi) * 0.1
            posisi = st.session_state.posisi

            placeholder.markdown(f"""
            <div style="
                height:280px;
                background:linear-gradient(to top, #2563eb, #93c5fd);
                border-radius:15px;
                position:relative;
                overflow:hidden;
            "> 
                     <div style="
                width:60px;
                height:60px;
                background:linear-gradient(145deg, #f87171, #ef4444);
                position:absolute;
                left:50%;
                transform:translateX(-50%);
                bottom:{posisi}px;
                border-radius:15px;
                box-shadow:0 10px 20px rgba(0,0,0,0.3);
            "></div>
             </div>
            """, unsafe_allow_html=True)

            time.sleep(speed)

# =====================
# GAME
# =====================
elif menu == "🎮 Game":
    st.title("🎮 Hitung Gaya Apung")

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
    Berapa gaya apung benda?
    </div>
    """, unsafe_allow_html=True)

    pilihan = [Fa, Fa + 2000, Fa - 2000]
    random.shuffle(pilihan)

    jawaban_user = st.radio("Pilih jawaban:", pilihan)

    if st.button("Cek Jawaban"):
        if jawaban_user == Fa:
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
