import streamlit as st
st.title("App con Streamlit")
sidebar = st.sidebar
sidebar.title("Esta es el Sidebar.")
sidebar.write("Datos del Sidebar.")
# Agregamos headers a la seccion principal
st.header("Header 1")
st.header("Headre 2 ")
# Agregamos texto a la seccion principal
st.write("Datos del content")

