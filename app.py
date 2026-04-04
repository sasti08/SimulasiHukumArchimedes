import streamlit as st
import time
import random

st.set_page_config(page_title="Archimedes App", page_icon="🌊")

# =====================
# NAVIGATION
# =====================
menu = st.sidebar.selectbox("Pilih Menu", ["🏠 Home", "🌊 Simulasi", "🎮 Game", "📝 Latihan"])

# =====================
# HOME
# =====================
if menu == "🏠 Home":
    st.title("🌊 Hukum Archimedes")
    st.write("Belajar gaya apung jadi seru, interaktif, dan mudah dipahami!")

    st.markdown("""
    ### 📘 Rumus:
    Fa = ρ × g × V

    - ρ = massa jenis fluida  
    - g = gravitasi  
    - V = volume benda tercelup  

    ### 📌 Konsep:
    - Fa > W → Terapung  
    - Fa = W → Melayang  
    - Fa < W → Tenggelam  
    """)

# =====================
# SIMULASI
# =====================
elif menu == "🌊 Simulasi":

    st.title("🌊 Simulasi Archimedes")

    rho = st.slider("Massa jenis fluida", 500, 1500, 1000)
    volume = st.slider("Volume", 1, 10, 3)
    massa = st.slider("Massa benda", 1, 10, 5)

    g = 9.8
    Fa = rho * g * volume
    W = massa * g

    st.write(f"Gaya Apung: {Fa:.2f}")
    st.write(f"Berat Benda: {W:.2f}")

    if Fa > W:
        kondisi = "terapung"
        st.success("🟢 Terapung")
    elif Fa == W:
        kondisi = "melayang"
        st.info("🟡 Melayang")
    else:
        kondisi = "tenggelam"
        st.error("🔴 Tenggelam")

    # animasi
    placeholder = st.empty()
    posisi = 20

    for i in range(25):
        if kondisi == "terapung":
            posisi += 3
        elif kondisi == "tenggelam":
            posisi -= 3
        else:
            posisi = 60

        posisi = max(10, min(150, posisi))

        placeholder.markdown(f"""
        <div style="height:250px;background:lightblue;position:relative;border-radius:10px;">
            <div style="width:50px;height:50px;background:red;
            position:absolute;left:50%;transform:translateX(-50%);
            bottom:{posisi}px;border-radius:10px;"></div>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(0.05)

# =====================
# GAME
# =====================
elif menu == "🎮 Game":

    st.title("🎮 Tebak Yuk!")

    rho = random.randint(500, 1500)
    volume = random.randint(1, 10)
    massa = random.randint(1, 10)

    g = 9.8
    Fa = rho * g * volume
    W = massa * g

    st.write(f"ρ = {rho}, V = {volume}, m = {massa}")

    jawaban = st.radio("Menurut kamu:", ["Terapung", "Melayang", "Tenggelam"])

    if st.button("Cek Jawaban"):

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
        {
            "q": "Benda dengan Fa lebih besar dari berat akan?",
            "opsi": ["Tenggelam", "Terapung", "Meleleh"],
            "jawab": "Terapung"
        },
        {
            "q": "Jika Fa = W maka benda?",
            "opsi": ["Terapung", "Melayang", "Hilang"],
            "jawab": "Melayang"
        }
    ]

    skor = 0

    for i, s in enumerate(soal):
        jawab = st.radio(s["q"], s["opsi"], key=i)
        if jawab == s["jawab"]:
            skor += 1

    if st.button("Lihat Skor"):
        st.write(f"Skor kamu: {skor}/{len(soal)}")
