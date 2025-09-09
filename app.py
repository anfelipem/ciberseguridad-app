import streamlit as st

# Título
st.title("🛡️ Ciberseguridad - Simulación de Alertas")
st.subheader("Aplicación educativa con Método Científico")

# Descripción
st.write("""
Esta app muestra cómo aplicar el **método científico** para investigar 
un fenómeno de ciberseguridad: la llegada de alertas de PUA y malware 
cuando el firewall cae y la puerta de enlace se desconecta.
""")

# Simulación de datos
firewall_status = st.selectbox("Estado del Firewall", ["Activo", "Caído"])
gateway_status = st.selectbox("Estado de la Puerta de Enlace", ["Conectada", "Desconectada"])

# Lógica simple de la app
if firewall_status == "Caído" or gateway_status == "Desconectada":
    st.error("⚠️ ALERTA: Riesgo elevado de ataques (PUA/Malware detectados)")
    st.write("👉 Recomendación: Revisar redundancia de firewall y activar alertas automáticas.")
else:
    st.success("✅ Sistema protegido: No se detectan riesgos significativos.")

# Espacio para aplicar método científico
st.markdown("## Método Científico aplicado")

observacion = st.text_area("1️⃣ Observación")
pregunta = st.text_area("2️⃣ Pregunta")
hipotesis = st.text_area("3️⃣ Hipótesis")
experimento = st.text_area("4️⃣ Experimentación")
analisis = st.text_area("5️⃣ Análisis de datos")
conclusion = st.text_area("6️⃣ Conclusiones")
comunicacion = st.text_area("7️⃣ Comunicación")

if st.button("📊 Guardar resultados"):
    st.write("### Resumen del grupo")
    st.write(f"- **Observación:** {observacion}")
    st.write(f"- **Pregunta:** {pregunta}")
    st.write(f"- **Hipótesis:** {hipotesis}")
    st.write(f"- **Experimentación:** {experimento}")
    st.write(f"- **Análisis de datos:** {analisis}")
    st.write(f"- **Conclusiones:** {conclusion}")
    st.write(f"- **Comunicación:** {comunicacion}")
