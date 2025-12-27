import streamlit as st

st.title("Peluquería XYZ")
st.write("¡Bienvenido a nuestra peluquería! Reserve su cita.")

# Ejemplo de servicio
servicios = ["Corte de cabelo", "Barba", "Coloração", "Tratamento"]
servicio_seleccionado = st.selectbox("Seleccione un servicio", servicios)

# Ejemplo de reserva (simplificado)
nombre = st.text_input("Su nombre")
if st.button("Reservar"):
    st.success(f"Cita reservada para {nombre} para {servicio_seleccionado}. ¡Gracias!")

