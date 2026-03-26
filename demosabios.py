import streamlit as st
import google.generativeai as genai

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Mesa de los Sabios", layout="wide")

# CONEXIÓN DEL MOTOR
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    motor_listo = True
except:
    motor_listo = False

# ESTILO DE LETRA GIGANTE
st.markdown("""
<style>
div.stTextArea textarea { font-size: 24px !important; font-weight: bold !important; }
.stMarkdown h3 { font-size: 30px !important; color: #1E88E5 !important; }
</style>
""", unsafe_allow_html=True)

# INTERFAZ
st.markdown("# 🏛️ La Mesa Redonda de los Sabios")
dolor = st.text_area("🎯 ESCRIBA EL DOLOR DEL CLIENTE AQUÍ:", height=150)

if st.button("🏛️ INICIAR DEBATE"):
    if dolor and motor_listo:
        # PANTALLA DINÁMICA DE ESTADO (LETRA GRANDE)
        aviso = st.empty()
        
        aviso.info("### 🧠 1/3: El Estratega está analizando...")
        p1 = modelo.generate_content(f"Actúa como Estratega. Plan para: {dolor}").text
        
        aviso.warning("### 🎭 2/3: El Animador y el Vigía debaten...")
        p2 = modelo.generate_content(f"Critica este plan: {p1}").text
        
        aviso.success("### ✍️ 3/3: Redactando Resumen Ejecutivo...")
        resumen = modelo.generate_content(f"Crea un resumen final de este debate: {p2}").text
        
        aviso.empty() # Limpiamos el aviso
        st.markdown("## 📜 RESULTADO FINAL")
        st.info(resumen)
    else:
        st.error("Asegúrese de escribir el dolor y que la llave API esté configurada.")
