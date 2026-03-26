import streamlit as st
import google.generativeai as genai

# CONFIGURACIÓN DE PÁGINA PARA ESPACIO DE LECTURA LIMPIO
st.set_page_config(page_title="Mesa de los Sabios", layout="wide")

# CONEXIÓN DEL MOTOR (USANDO LA LLAVE GUARDADA)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    motor_listo = True
except:
    motor_listo = False

# ESTILO DE LETRA GIGANTE (PARA EL ARQUITECTO)
st.markdown("""
<style>
    /* Texto de entrada gigante */
    div.stTextArea textarea { font-size: 25px !important; font-weight: bold !important; color: #1E3A8A !important; }
    /* Títulos gigantes */
    h1 { font-size: 50px !important; }
    h2 { font-size: 40px !important; }
    h3 { font-size: 30px !important; }
    /* Botón grande */
    .stButton>button { height: 3em; font-size: 25px !important; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

# INTERFAZ PRINCIPAL
st.markdown("# 🏛️ La Mesa Redonda de los Sabios")
st.markdown("---")

st.markdown("### 🎯 ESCRIBA EL DOLOR DEL CLIENTE AQUÍ:")
dolor = st.text_area("", height=200, placeholder="Describa la situación...")

if st.button("🏛️ INICIAR EL DEBATE DE LOS SABIOS", use_container_width=True):
    if dolor and motor_listo:
        # PANTALLA DINÁMICA DE ESTADO (LETRA GRANDE Y CLARA)
        aviso = st.empty()
        
        aviso.info("## 🧠 1/3: El Estratega está analizando la situación...")
        res1 = modelo.generate_content(f"Actúa como Estratega. Plan lógico para: {dolor}").text
        
        aviso.warning("## 🎭 2/3: El Animador y el Vigía están debatiendo los riesgos...")
        res2 = modelo.generate_content(f"Analiza este plan desde la emoción y el riesgo: {res1}").text
        
        aviso.success("## ✍️ 3/3: El Sintetizador está redactando el Resumen Ejecutivo...")
        final = modelo.generate_content(f"Crea un resumen ejecutivo final en viñetas claras basado en: {res2}").text
        
        aviso.empty() # Limpiamos los avisos para dejar el trono limpio
        
        st.markdown("## 📜 RESUMEN EJECUTIVO FINAL")
        st.info(final)
    elif not motor_listo:
        st.error("⚠️ Error: La llave del motor no está conectada.")
    else:
        st.warning("⚠️ Por favor, escriba el dolor del cliente para comenzar.")
