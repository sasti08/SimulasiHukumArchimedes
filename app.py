import streamlit as st
import time

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
# SIMULASI PRO
# =====================
elif menu == "🌊 Simulasi":
    st.title("🌊 Simulasi Archimedes")
    
    # Input parameters
    col1, col2, col3 = st.columns(3)
    with col1:
        rho = st.slider("Massa jenis fluida (kg/m³)", 500, 1500, 1000)
    with col2:
        volume = st.slider("Volume benda (m³)", 0.1, 5.0, 1.0)
    with col3:
        massa = st.slider("Massa benda (kg)", 0.1, 10.0, 2.0)

    g = 9.8
    Fa = rho * g * volume
    W = massa * g

    # Tentukan kondisi dan target posisi (0=dasar, 140=tengah, 260=atas)
    if Fa > W:
        kondisi = "TERAPUNG"
        target = 260  # Posisi atas (di atas air)
        warna_status = "🟢"
        status_bg = "#dcfce7"
    elif abs(Fa - W) < 0.1:  # Toleransi kecil untuk ==
        kondisi = "MELAYANG"
        target = 140  # Posisi tengah (di tengah air)
        warna_status = "🟡"
        status_bg = "#fef3c7"
    else:
        kondisi = "TENGGELAM"
        target = 0    # Posisi dasar (di bawah)
        warna_status = "🔴"
        status_bg = "#fecaca"

    # Info gaya dalam card
    st.markdown(f"""
    <div class="card">
    <h4>📊 Data Perhitungan</h4>
    <div style="display: flex; gap: 20px;">
        <div><b>Gaya Apung:</b><br>{Fa:.1f} N</div>
        <div><b>Berat Benda:</b><br>{W:.1f} N</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Status kondisi
    st.markdown(f"""
    <div class="card" style="background: {status_bg}; border-left: 5px solid {warna_status[1:]};">
        <h3>{warna_status} {kondisi}</h3>
        <p><b>{warna_status} {kondisi}:</b> Bola berada di posisi yang sesuai dengan hukum Archimedes!</p>
    </div>
    """, unsafe_allow_html=True)

    # Inisialisasi session state
    if "posisi" not in st.session_state:
        st.session_state.posisi = 140  # mulai di tengah

    # Update posisi dengan smoothing dan osilasi kecil
    t = time.time()
    posisi = st.session_state.posisi
    
    # Gerak ke target dengan smoothing
    posisi += (target - posisi) * 0.15
    
    # Osilasi kecil untuk efek realistis (hanya saat stabil)
    if abs(posisi - target) < 20:
        posisi += 3 * math.sin(t * 2)
    
    # Batasi posisi
    posisi = max(0, min(280, posisi))
    st.session_state.posisi = posisi

    # Visualisasi dengan air di tengah
    st.markdown(f"""
    <div class="card">
        <h4>🎬 Simulasi Visual</h4>
        <div style="
            height: 320px;
            background: linear-gradient(to bottom, 
                #e0f2fe 0%, 
                #e0f2fe 45%, 
                #0ea5e9 45%, 
                #0284c7 55%, 
                #0369a1 100%);
            border-radius: 20px;
            position: relative;
            overflow: hidden;
            box-shadow: inset 0 4px 8px rgba(0,0,0,0.1);
        ">
            <!-- Garis permukaan air -->
            <div style="
                position: absolute;
                top: 50%;
                left: 0;
                right: 0;
                height: 2px;
                background: rgba(255,255,255,0.6);
                box-shadow: 0 0 10px rgba(255,255,255,0.8);
            "></div>
            
            <!-- Label posisi -->
            <div style="position:absolute; top:10px; left:10px; color:#1e40af; font-weight:bold;">
                Permukaan Air
            </div>
            <div style="position:absolute; bottom:10px; left:10px; color:#1e40af; font-weight:bold;">
                Dasar Wadah
            </div>
            
            <!-- Bola benda -->
            <div style="
                width: 70px;
                height: 70px;
                background: radial-gradient(circle at 30% 30%, #f87171, #dc2626);
                position: absolute;
                left: 50%;
                transform: translateX(-50%);
                bottom: {posisi}px;
                border-radius: 50%;
                box-shadow: 
                    0 15px 30px rgba(0,0,0,0.4),
                    inset 0 2px 4px rgba(255,255,255,0.3);
                border: 3px solid rgba(255,255,255,0.8);
                transition: bottom 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            ">
                <div style="
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    width: 20px;
                    height: 20px;
                    background: rgba(255,255,255,0.6);
                    border-radius: 50%;
                    box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
                "></div>
            </div>
            
            <!-- Efek riak air saat di tengah -->
            {'<div style="position:absolute; bottom:140px; left:50%; transform:translateX(-50%); width:100px; height:100px; border:2px solid rgba(255,255,255,0.3); border-radius:50%; animation: ripple 2s infinite;"></div>' if abs(posisi-140)<20 else ''}
        </div>
        
        <!-- Keterangan posisi -->
        <div style="margin-top:15px; text-align:center;">
            <div style="font-size:18px; font-weight:bold; color:#1e40af;">
                Posisi bola: {posisi:.0f}px dari dasar
            </div>
            <div style="color:#6b7280;">
                {'🟢 TERAPUNG: >250px (di atas air)' if target==260 else 
                 '🟡 MELAYANG: ~140px (di tengah air)' if target==140 else 
                 '🔴 TENGGELAM: 0px (di dasar)'}
            </div>
        </div>
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
