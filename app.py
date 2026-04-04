import streamlit as st
import time
import random

st.set_page_config(page_title="Archimedes Pro Max", page_icon="🌊", layout="centered")

# =====================
# STYLE (BIAR AESTHETIC)
# =====================
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #dbeafe, #eff6ff);
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
    <h3>📘 Rumus</h3>
    Fa = ρ × g × V <br><br>
    
    <b>Konsep:</b><br>
    🟢 Fa > W → Terapung <br>
    🟡 Fa = W → Melayang <br>
    🔴 Fa < W → Tenggelam
    </div>
    """, unsafe_allow_html=True)

# =====================
# SIMULASI PRO
# =====================
st.subheader("🌊 Simulasi Gerakan")

# INIT STATE
if "jalan" not in st.session_state:
    st.session_state.jalan = False

if "posisi" not in st.session_state:
    st.session_state.posisi = 20

# BUTTON CONTROL
col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start"):
        st.session_state.jalan = True

with col2:
    if st.button("⏹ Stop"):
        st.session_state.jalan = False

speed = st.slider("Kecepatan", 0.01, 0.2, 0.05)

# TARGET POSISI
if kondisi == "terapung":
    target = 150
elif kondisi == "melayang":
    target = 80
else:
    target = 10

placeholder = st.empty()

# LOOP JALAN TERUS
while st.session_state.jalan:

    # gerakan smooth
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

    st.title("🎮 Tebak Kondisi")

    rho = random.randint(500, 1500)
    volume = random.randint(1, 10)
    massa = random.randint(1, 10)

    g = 9.8
    Fa = rho * g * volume
    W = massa * g

    st.markdown(f"""
    <div class="card">
    ρ = {rho} <br>
    V = {volume} <br>
    m = {massa}
    </div>
    """, unsafe_allow_html=True)

    jawaban = st.radio("Tebak:", ["Terapung", "Melayang", "Tenggelam"])

    if st.button("Cek"):
        if Fa > W:
            benar = "Terapung"
        elif Fa == W:
            benar = "Melayang"
        else:
            benar = "Tenggelam"

        if jawaban == benar:
            st.success("🎉 Benar!")
        else:
            st.error(f"❌ Salah! Jawaban: {benar}")

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
