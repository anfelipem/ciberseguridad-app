import streamlit as st

st.title("🛡️ Método Científico en Ciberseguridad")
st.subheader("Ejercicio práctico en grupos")

st.write("**Fenómeno a investigar:** Se registraron alertas de PUA y malware cuando el firewall cayó y la puerta de enlace se desconectó.")

# Etapas del método científico
observacion = st.text_area("1️⃣ Observación")
pregunta = st.text_area("2️⃣ Pregunta")
hipotesis = st.text_area("3️⃣ Hipótesis")
experimento = st.text_area("4️⃣ Experimentación")
analisis = st.text_area("5️⃣ Análisis de datos")
conclusion = st.text_area("6️⃣ Conclusiones")
comunicacion = st.text_area("7️⃣ Comunicación")

if st.button("✅ Guardar respuestas"):
    st.success("Tus respuestas fueron registradas.")
    st.write("### 📊 Resumen del grupo:")
    st.write("- **Observación:**", observacion)
    st.write("- **Pregunta:**", pregunta)
    st.write("- **Hipótesis:**", hipotesis)
    st.write("- **Experimentación:**", experimento)
    st.write("- **Análisis de datos:**", analisis)
    st.write("- **Conclusiones:**", conclusion)
    st.write("- **Comunicación:**", comunicacion)
