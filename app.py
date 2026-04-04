import streamlit as st

st.set_page_config(page_title="Simulasi Archimedes", page_icon="🌊")

# ======================
# STYLE (BIAR MIRIP UI KAMU)
# ======================
st.markdown("""
<style>
body {
    background-color: #cbd5e1;
}
.card {
    background: #e5e7eb;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
}
.simulasi-box {
    background: #e5e7eb;
    border-radius: 20px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# JUDUL
# ======================
st.title("🧊 Simulasi Hukum Archimedes")

# ======================
# INPUT CARD
# ======================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Bandingkan massa jenis")

rho_benda = st.number_input("Massa jenis benda", value=100.0)
rho_air = st.number_input("Massa jenis fluida", value=50.0)

if st.button("Simulasikan"):
    if rho_benda < rho_air:
        status = "Mengapung 🟢"
        posisi = 120
    elif rho_benda == rho_air:
        status = "Melayang 🟡"
        posisi = 80
    else:
        status = "Tenggelam 🔴"
        posisi = 20

    st.session_state.status = status
    st.session_state.posisi = posisi

# tampilkan status
if "status" in st.session_state:
    st.write(f"Status: {st.session_state.status}")

st.markdown('</div>', unsafe_allow_html=True)

# ======================
# SIMULASI VISUAL
# ======================
st.markdown('<div class="simulasi-box">', unsafe_allow_html=True)

posisi = st.session_state.get("posisi", 80)

st.markdown(f"""
<div style="
    height:300px;
    position:relative;
    border-radius:20px;
    overflow:hidden;
    background:#e5e7eb;
">

    <!-- air -->
    <div style="
        position:absolute;
        bottom:0;
        width:100%;
        height:50%;
        background:#93c5fd;
    "></div>

    <!-- benda -->
    <div style="
        width:70px;
        height:70px;
        background:#8b5a2b;
        position:absolute;
        left:50%;
        transform:translateX(-50%);
        bottom:{posisi}px;
        border-radius:5px;
    "></div>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
