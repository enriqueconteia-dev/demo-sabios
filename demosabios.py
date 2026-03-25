import streamlit as st
import google.generativeai as genai
import os

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

dolor_cliente = st.text_area("", height=200, disabled=bloqueado)

st.markdown("---")
st.markdown("# 📦 ENTREGABLES DE EL CONSTRUCTOR")

if bloqueado:
    st.warning("⚠️ El sistema se ha bloqueado de forma segura tras alcanzar el límite global de demostración. Gracias por experimentar el poder de El Artefacto.")
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 👉 RUTA PRINCIPAL")
        if st.button("🛠️ Generar Prompt (Consumir 1 Token)"):
            registrar_uso()
            st.success("¡Sabiduría procesada! (Aquí aparecería el resultado). Se ha descontado 1 token.")
            st.rerun()
    with col2:
        st.markdown("### 👉 RUTA TÉCNICA")
        st.button("🐍 Código Python (Desactivado en Demo)")
    with col3:
        st.markdown("### 👉 RUTA VISUAL")
        st.button("🌐 Código HTML (Desactivado en Demo)")