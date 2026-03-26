import streamlit as st
import google.generativeai as genai
import os

# ==========================================
# CONFIGURACIÓN DE LA API DE GOOGLE
# ==========================================
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.warning("⚠️ Falta configurar la clave de API (GEMINI_API_KEY) en los Secrets.")

# ==========================================
# MEMORIA PARA LA INTERFAZ LIMPIA
# ==========================================
if "veredicto" not in st.session_state:
    st.session_state.veredicto = ""

# ==========================================
# EL CONTADOR GLOBAL DE 7 USOS (LA TRAMPA)
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
# CONFIGURACIÓN Y ESTILO VISUAL (Cara Imponente)
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

# ==========================================
# PANEL DE CONTROL (Adaptado para la Demo)
# ==========================================
with st.sidebar:
    st.markdown("## ⚙️ Estado del Sistema")
    st.markdown("---")
    
    if bloqueado:
        st.error("🛑 SESIÓN DE CORTESÍA FINALIZADA")
        st.write("El equipo directivo ha consumido los 7 tokens de prueba global.")
    else:
        st.success("🟢 SISTEMA ACTIVO")
        st.write(f"**Tokens restantes:** {usos_restantes} de {LIMITE_USOS}")
        
    st.markdown("---")
    st.info("Para obtener acceso ilimitado a El Artefacto, contacte al Arquitecto.")

# ==========================================
# INTERFAZ PRINCIPAL
# ==========================================
st.markdown("# 🏛️ El Trono del Arquitecto (Versión Demo)")
st.markdown("### *Mesa de los Sabios: Inteligencia Colectiva Soberana*")
st.markdown("---")

st.markdown("## 🧠 El Consejo de Sabios en Sesión:")
st.markdown("### ♟️ EL ESTRATEGA | 🎭 EL ANIMADOR | 🦉 EL VIGÍA | 🏗️ EL CONSTRUCTOR")
st.markdown("---")

st.markdown("## 🎯 EL DOLOR / DIFICULTAD DEL CLIENTE (¡CRÍTICO!)")
st.markdown("### Describa aquí el desafío comercial a solucionar:")

dolor_cliente = st.text_area("", height=200, disabled=bloqueado, label_visibility="collapsed")

st.markdown("---")
st.markdown("# 📦 ENTREGABLES DE EL CONSTRUCTOR")

if bloqueado:
    st.warning("⚠️ El sistema se ha bloqueado de forma segura tras alcanzar el límite global de demostración. Gracias por experimentar el poder de El Artefacto.")
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 👉 RUTA PRINCIPAL")
        if st.button("🛠️ Generar Prompt (Consumir 1 Token)"):
            if dolor_cliente:
                with st.spinner("Los Sabios están deliberando..."):
                    try:
                        # Llamada real a la IA
                        model = genai.GenerativeModel('gemini-1.5-pro')
                        respuesta = model.generate_content(dolor_cliente)
                        
                        # Guardamos la respuesta en la memoria y cobramos el token
                        st.session_state.veredicto = respuesta.text
                        registrar_uso()
                        st.rerun() # Recarga para actualizar el contador lateral
                    except Exception as e:
                        st.error(f"Error de comunicación con los Sabios: {e}")
            else:
                st.warning("Por favor, describa el desafío antes de consultar.")
                
    with col2:
        st.markdown("### 👉 RUTA TÉCNICA")
        st.button("🐍 Código Python (Desactivado en Demo)")
    with col3:
        st.markdown("### 👉 RUTA VISUAL")
        st.button("🌐 Código HTML (Desactivado en Demo)")

# ==========================================
# EL ESPACIO LIMPIO PARA LA LECTURA (Abajo de todo)
# ==========================================
if st.session_state.veredicto:
    st.divider()
    st.markdown("## 📜 El Veredicto de los Sabios")
    st.write(st.session_state.veredicto)
