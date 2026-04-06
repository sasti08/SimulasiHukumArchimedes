elif menu == "🌊 Simulasi":
    st.title("🌊 Simulasi Archimedes")

    # Input manual
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
    from streamlit_autorefresh import st_autorefresh
    import math, time
    st_autorefresh(interval=50, limit=None, key="refresh_sim")

    # Inisialisasi posisi balok
    if "posisi" not in st.session_state:
        st.session_state.posisi = target

    # Hitung posisi balok dengan osilasi
    t = time.time()
    posisi = st.session_state.posisi
    posisi += (target - posisi) * 0.1       # smoothing ke target
    posisi += 10 * math.sin(t * 3)          # osilasi halus
    st.session_state.posisi = posisi

    # Render balok dan air
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
