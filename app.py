import streamlit as st
import time

st.set_page_config(page_title="Simulasi Archimedes Pro", page_icon="🌊")

# =====================
# JUDUL
# =====================
st.title("🌊 Simulasi Hukum Archimedes (Pro)")
st.write("Belajar gaya apung dengan simulasi interaktif yang smooth dan realistis 😎")

# =====================
# INPUT
# =====================
st.subheader("🔧 Input Data")

rho = st.slider("Massa jenis fluida (kg/m³)", 500, 1500, 1000)
volume = st.slider("Volume benda (m³)", 0.1, 5.0, 1.0)
massa = st.slider("Massa benda (kg)", 0.1, 10.0, 2.0)

g = 9.8

# =====================
# PERHITUNGAN
# =====================
Fa = rho * g * volume
W = massa * g

# =====================
# OUTPUT
# =====================
st.subheader("📊 Hasil")

col1, col2 = st.columns(2)

with col1:
    st.metric("Gaya Apung (N)", f"{Fa:.2f}")

with col2:
    st.metric("Berat Benda (N)", f"{W:.2f}")

# =====================
# ANALISIS
# =====================
st.subheader("📌 Analisis")

if Fa > W:
    kondisi = "terapung"
    st.success("🟢 Benda Terapung")
elif Fa == W:
    kondisi = "melayang"
    st.info("🟡 Benda Melayang")
else:
    kondisi = "tenggelam"
    st.error("🔴 Benda Tenggelam")

# =====================
# SIMULASI PRO GACOR 🔥
# =====================
st.subheader("🌊 Simulasi Gerakan (Pro Mode)")

# kontrol
col1, col2 = st.columns(2)
with col1:
    start = st.button("▶️ Start Simulasi")
with col2:
    speed = st.slider("Kecepatan Animasi", 0.01, 0.2, 0.05)

# target posisi
if kondisi == "terapung":
    target = 150
elif kondisi == "melayang":
    target = 80
else:
    target = 10

# posisi awal
if "posisi" not in st.session_state:
    st.session_state.posisi = 20

placeholder = st.empty()

# animasi
if start:
    for i in range(60):

        # gerakan smooth (easing)
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
        
        <!-- efek air -->
        <div style="
            position:absolute;
            top:0;
            width:100%;
            height:40px;
            background:rgba(255,255,255,0.3);
            border-radius:50%;
            filter:blur(10px);
        "></div>

        <!-- benda -->
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
            transition:all 0.1s;
        "></div>

        </div>
        """, unsafe_allow_html=True)

        time.sleep(speed)

# =====================
# PENJELASAN
# =====================
st.subheader("📖 Penjelasan")

if kondisi == "terapung":
    st.write("Gaya apung lebih besar dari berat benda, sehingga benda naik ke permukaan.")
elif kondisi == "melayang":
    st.write("Gaya apung sama dengan berat benda, sehingga benda berada di tengah fluida.")
else:
    st.write("Gaya apung lebih kecil dari berat benda, sehingga benda tenggelam.")
