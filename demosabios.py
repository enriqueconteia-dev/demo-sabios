import streamlit as st
import google.generativeai as genai
import os

# Configuración de la página para maximizar el espacio de lectura
st.set_page_config(page_title="Mesa de los Sabios", layout="centered")

# Configuración de la API (Asumiendo que la clave está configurada en los secrets de Streamlit)
# Si usa otra forma de poner la clave, reemplácela aquí.
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.warning("Falta configurar la clave de API de Google (GEMINI_API_KEY) en los Secrets de Streamlit.")

# Títulos de la aplicación
st.title("🏛️ Trono del Arquitecto")
st.header("Mesa de los Sabios")

# Área de entrada para el usuario
st.markdown("**Escribe aquí tu tema o pregunta para los Sabios:**")
consulta = st.text_area("", height=150, label_visibility="collapsed")

# Botón de acción
if st.button("Convocar a los Sabios"):
    if consulta:
        with st.spinner("Los Sabios están deliberando..."):
            try:
                # Llamada al modelo de IA
                model = genai.GenerativeModel('gemini-1.5-pro')
                respuesta = model.generate_content(consulta)
                
                # Línea separadora sutil
                st.divider()
                
                # Espacio limpio y prioritario para la lectura de la respuesta
                st.markdown("### 📜 El Veredicto de los Sabios")
                st.write(respuesta.text)
                
            except Exception as e:
                st.error(f"Hubo un error en la comunicación con los Sabios: {e}")
    else:
        st.warning("Por favor, escribe una consulta antes de convocar a los Sabios.")
