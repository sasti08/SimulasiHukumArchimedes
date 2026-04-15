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

    # INPUT MANUAL (NO SLIDER)
    col1, col2, col3 = st.columns(3)

    with col1:
        rho_fluida = st.number_input("ρ Fluida (kg/m³)", min_value=0.0, value=1000.0)

    with col2:
        volume = st.number_input("Volume (m³)", min_value=0.01, value=1.0, format="%.2f")

    with col3:
        massa = st.number_input("Massa (kg)", min_value=0.01, value=2.0, format="%.2f")

    g = 9.8

    # PERHITUNGAN
    rho_benda = massa / volume
    Fa = rho_fluida * g * volume
    W = massa * g

    # LOGIKA KONDISI
    if rho_benda < rho_fluida:
        kondisi = "Terapung"
        warna = "🟢"
        target = 180
    elif abs(rho_benda - rho_fluida) < 0.01:
        kondisi = "Melayang"
        warna = "🟡"
        target = 100
    else:
        kondisi = "Tenggelam"
        warna = "🔴"
        target = 20

    # SESSION STATE
    if "jalan" not in st.session_state:
        st.session_state.jalan = False
    if "posisi" not in st.session_state:
        st.session_state.posisi = 50

    # BUTTON
    if st.button("▶️ Start / Stop Simulasi"):
        st.session_state.jalan = not st.session_state.jalan

    # INFO (AUTO UPDATE)
    st.markdown(f"""
    <div class="card">
    <b>Status:</b> {warna} {kondisi} <br><br>

    ρ benda = <b>{rho_benda:.2f}</b><br>
    ρ fluida = <b>{rho_fluida}</b><br><br>

    Gaya Apung = <b>{Fa:.2f} N</b><br>
    Berat = <b>{W:.2f} N</b><br><br>

    <b>Keterangan:</b><br>
    ρ benda &lt; ρ fluida → Terapung<br>
    ρ benda = ρ fluida → Melayang<br>
    ρ benda &gt; ρ fluida → Tenggelam
    </div>
    """, unsafe_allow_html=True)

    placeholder = st.empty()

    # ANIMASI
    if st.session_state.jalan:
        for i in range(80):
            st.session_state.posisi += (target - st.session_state.posisi) * 0.15
            st.session_state.posisi += math.sin(i * 0.3) * 2

            placeholder.markdown(f"""
            <div style="
                height:280px;
                background:#2563eb;
                border-radius:15px;
                position:relative;
                overflow:hidden;
            ">                         
                <div style="
                    width:60px;
                    height:60px;
                    background:#8B4513;
                    position:absolute;
                    left:50%;
                    transform:translateX(-50%);
                    bottom:{st.session_state.posisi}px;
                    border-radius:5px;
                "></div> 
            </div>
            """, unsafe_allow_html=True)

            time.sleep(0.05)

        st.rerun()

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
