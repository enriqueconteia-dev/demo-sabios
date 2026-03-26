import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mesa de los Sabios", layout="wide")

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    motor_listo = True
except:
    motor_listo = False

st.markdown("<style>div.stTextArea textarea { font-size: 25px !important; font-weight: bold !important; } h1 { font-size: 50px !important; } .stButton>button { height: 3em; font-size: 25px !important; }</style>", unsafe_allow_html=True)

st.markdown("# 🏛️ La Mesa Redonda de los Sabios")
st.markdown("---")
dolor = st.text_area("🎯 ESCRIBA EL DOLOR DEL CLIENTE AQUÍ:", height=200)

if st.button("🏛️ INICIAR EL DEBATE DE LOS SABIOS", use_container_width=True):
    if dolor and motor_listo:
        aviso = st.empty()
        aviso.info("## 🧠 1/3: El Estratega está analizando...")
        res1 = modelo.generate_content(f"Actúa como Estratega. Plan para: {dolor}").text
        aviso.warning("## 🎭 2/3: El Animador y el Vigía debaten...")
        res2 = modelo.generate_content(f"Analiza este plan: {res1}").text
        aviso.success("## ✍️ 3/3: El Sintetizador redacta el final...")
        final = modelo.generate_content(f"Resumen ejecutivo final de: {res2}").text
        aviso.empty()
        st.markdown("## 📜 RESUMEN EJECUTIVO FINAL")
        st.info(final)
    else:
        st.error("Por favor escriba el dolor del cliente.")
