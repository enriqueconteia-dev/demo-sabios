import streamlit as st
import google.generativeai as genai
import os

# ==========================================
# EL CONTADOR GLOBAL DE 7 USOS
# ==========================================
ARCHIVO_CONTADOR = "libreta_global.txt"
LIMITE_USOS = 7

def obtener_usos():
    if not os.path.exists(ARCHIVO_CONTADOR):
        return 0
    with open(ARCHIVO_CONTADOR, "r") as f:
        try:
            return int(f.read().strip())
        except:
            return 0

def registrar_uso():
    usos_actuales = obtener_usos()
    with open(ARCHIVO_CONTADOR, "w") as f:
        f.write(str(usos_actuales + 1))

usos_realizados = obtener_usos()
usos_restantes = LIMITE_USOS - usos_realizados
bloqueado = usos_restantes <= 0

# ==========================================
# CONEXIÓN DEL CEREBRO (LLAVE INVISIBLE)
# ==========================================
try:
    # Intenta buscar la llave en la caja fuerte de Streamlit
    llave = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=llave)
    motor_listo = True
except:
    motor_listo = False

# ==========================================
# CONFIGURACIÓN Y ESTILO VISUAL
# ==========================================
st.set_page_config(page_title="Demo: El Trono del Arquitecto", layout="wide")

st.markdown("""
<style>
div.stTextArea textarea, 
div[data-baseweb="textarea"] textarea {
    font-size: 32px !important;  
    font-weight: 900 !important; 
    font-style: italic !important; 
    color: #000000 !important;   
    line-height: 1.5 !important;
}
div.stButton > button:first-child {
    background-color: #f0f8ff; 
    border: 2px solid #a8cfee;
    color: #004a99;
    font-weight: bold;
    transform: scale(1.03); 
    font-size: 20px !important; 
}
div.stButton > button:first-child:hover {
    background-color: #d8e6f1;
    border: 2px solid #8ab1d4;
}
</style>
""", unsafe_allow_html=True)

# Inicializar memoria para que el resultado no se borre
if 'resultado_sabios' not in st.session_state:
    st.session_state.resultado_sabios = ""

# ==========================================
# PANEL DE CONTROL
# ==========================================
with st.sidebar:
    st.markdown("## ⚙️ Estado del Sistema")
    st.markdown("---")
    
    if bloqueado:
        st.error("🛑 SESIÓN FINALIZADA")
        st.write("Se han consumido los 7 tokens.")
    else:
        st.success("🟢 SISTEMA ACTIVO")
        st.write(f"**Tokens restantes:** {usos_restantes} de {LIMITE_USOS}")
        
    st.markdown("---")
    if not motor_listo:
        st.warning("⚠️ Falta conectar la Llave en la Bóveda")

# ==========================================
# INTERFAZ PRINCIPAL
# ==========================================
st.markdown("# 🏛️ El Trono del Arquitecto (Versión Demo)")
st.markdown("### *Mesa de los Sabios: Inteligencia Colectiva Soberana*")
st.markdown("---")

st.markdown("## 🎯 EL DOLOR / DIFICULTAD DEL CLIENTE (¡CRÍTICO!)")
dolor_cliente = st.text_area("", height=200, disabled=bloqueado)

st.markdown("---")
st.markdown("# 📦 ENTREGABLES DE EL CONSTRUCTOR")

if bloqueado:
    st.warning("⚠️ Límite de demostración alcanzado. Contacte al Arquitecto.")
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 👉 RUTA PRINCIPAL")
        if st.button("🛠️ Generar Prompt (Consumir 1 Token)"):
            if dolor_cliente:
                registrar_uso()
                with st.spinner("🧠 Los Sabios están deliberando..."):
                    if motor_listo:
                        try:
                            # Aquí respira el verdadero cerebro
                            modelo = genai.GenerativeModel('gemini-1.5-flash')
                            instruccion = f"Actúa como un equipo de consultores expertos. El cliente tiene este dolor comercial: '{dolor_cliente}'. Escribe un análisis brillante y un Prompt para solucionar su problema."
                            respuesta = modelo.generate_content(instruccion)
                            st.session_state.resultado_sabios = respuesta.text
                        except Exception as e:
                            st.session_state.resultado_sabios = f"Error de conexión: {e}"
                    else:
                        st.session_state.resultado_sabios = "El motor está apagado. Falta la llave en la bóveda."
                st.rerun() 
            else:
                st.warning("⚠️ Maestro, escriba un dolor primero.")
    with col2:
        st.markdown("### 👉 RUTA TÉCNICA")
        st.button("🐍 Código Python (Desactivado)")
    with col3:
        st.markdown("### 👉 RUTA VISUAL")
        st.button("🌐 Código HTML (Desactivado)")

# ==========================================
# ESPACIO DE LECTURA (¡LO QUE FALTABA!)
# ==========================================
st.markdown("---")
st.markdown("# 🔍 Resultados de la Mesa de los Sabios")

# Aquí es donde aparecerá el diálogo
if st.session_state.resultado_sabios:
    st.info(st.session_state.resultado_sabios)
else:
    st.markdown("*(El análisis de los Sabios aparecerá aquí abajo de forma inminente tras consumir un token...)*")
