import streamlit as st
import google.generativeai as genai
import time
import os

# Instrucción técnica del Manual Maestro: pip install google-generativeai

# ==========================================
# CONEXIÓN DEL CEREBRO (LLAVE INVISIBLE)
# ==========================================
try:
    llave = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=llave)
    motor_listo = True
except:
    motor_listo = False

# ==========================================
# CONFIGURACIÓN Y ESTILO VISUAL LIMPIO
# ==========================================
st.set_page_config(page_title="El Trono del Arquitecto - Mesa Redonda", layout="wide")

st.markdown("""
<style>
div.stTextArea textarea {
    font-size: 24px !important;  
    font-weight: bold !important; 
    line-height: 1.4 !important;
}
</style>
""", unsafe_allow_html=True)

# Memoria de la sesión para mantener la pantalla limpia
if 'resumen_ejecutivo' not in st.session_state:
    st.session_state.resumen_ejecutivo = ""
if 'debate_completado' not in st.session_state:
    st.session_state.debate_completado = False

# ==========================================
# INTERFAZ PRINCIPAL
# ==========================================
st.markdown("# 🏛️ El Trono del Arquitecto")
st.markdown("### *Dinámica 2: La Mesa Redonda de los Sabios*")
st.markdown("---")

st.markdown("## 🎯 EL DOLOR / DIFICULTAD DEL CLIENTE")
dolor_cliente = st.text_area("", height=150, placeholder="Escriba aquí la situación del cliente...")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🏛️ Iniciar Mesa Redonda", use_container_width=True):
        if dolor_cliente and motor_listo:
            # CAMBIO ESTRATÉGICO: Usamos gemini-pro que es universal y no falla en la nube
            modelo = genai.GenerativeModel('gemini-pro')
            
            # EL MONITOR DE ESTADO (Los Cartelitos Dinámicos ahora GIGANTES)
            with st.status("🧠 Iniciando la deliberación en la sombra...", expanded=True) as status:
                
                # Paso 1: Apertura
                st.markdown("### ⏳ El Estratega está diagnosticando la estructura...")
                prompt_1 = f"Actúa como El Estratega. El cliente tiene este dolor: '{dolor_cliente}'. Diagnostica y propón un plan frío y lógico de 3 ejes."
                plan_inicial = modelo.generate_content(prompt_1).text
                
                # Paso 2: Revisión Cruzada
                st.markdown("### ⏳ El Animador y El Vigía están inyectando emoción y revisando riesgos...")
                prompt_2 = f"Actúa como El Animador. Lee este plan: '{plan_inicial}'. Critica su frialdad y propón un ángulo emocional."
                critica_animador = modelo.generate_content(prompt_2).text
                
                prompt_3 = f"Actúa como El Vigía. Lee este plan: '{plan_inicial}'. Señala riesgos éticos o de marca."
                critica_vigia = modelo.generate_content(prompt_3).text
                
                # Paso 3: Defensa
                st.markdown("### ⏳ El Estratega está defendiendo su postura...")
                prompt_4 = f"Actúa como El Estratega. Tus colegas dijeron esto. Animador: '{critica_animador}'. Vigía: '{critica_vigia}'. Ajusta tu plan inicial, defiende lo que creas necesario."
                plan_ajustado = modelo.generate_content(prompt_4).text
                
                # Paso 4: Réplica
                st.markdown("### ⏳ Derecho a réplica: Veredicto final de los colegas...")
                prompt_5 = f"Actúan como Animador y Vigía. El Estratega ajustó el plan a esto: '{plan_ajustado}'. Den su veredicto final rápido: ¿Aprueban o mantienen objeción?"
                replica_final = modelo.generate_content(prompt_5).text
                
                # Paso 5: Síntesis
                st.markdown("### ⏳ El Sintetizador está redactando el Resumen Ejecutivo final...")
                prompt_6 = f"Actúa como Sintetizador Ejecutivo. Lee este debate final: '{replica_final}' y el plan: '{plan_ajustado}'. Redacta un Resumen Ejecutivo en viñetas para el Director humano."
                st.session_state.resumen_ejecutivo = modelo.generate_content(prompt_6).text
                
                status.update(label="✅ Debate concluido. Pantalla lista.", state="complete", expanded=False)
            
            st.session_state.debate_completado = True
            st.rerun()

        elif not motor_listo:
            st.error("Falta conectar la llave del motor.")
        else:
            st.warning("Por favor, escriba el dolor del cliente.")

# ==========================================
# EL ESPACIO DE LECTURA (SOBERANÍA DEL CONSULTOR)
# ==========================================
if st.session_state.debate_completado:
    st.markdown("---")
    st.markdown("## 📜 Resumen Ejecutivo de los Sabios")
    st.info(st.session_state.resumen_ejecutivo)
    
    st.markdown("### ⚙️ Control de Mando")
    col_a, col_b = st.columns(2)
    with col_a:
        st.button("✅ Aprobar y Construir Prompt Final (Próximamente)")
    with col_b:
        st.text_input("✋ Exigir Cambios a la Mesa:", placeholder="Ej: Que el Animador sea más formal...")
        st.button("🔄 Reenviar al Debate")
