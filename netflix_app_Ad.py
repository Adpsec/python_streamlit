import streamlit as st
import pandas as pd
import numpy as np
import codecs

doc = 'movies.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(doc, index_col=0, encoding='latin-1')
    return data

def load_data_bydirector(name):
    data = pd.read_csv(doc, index_col=0, encoding='latin-1')
    filtered_data_bydirector = data[data["director"].str.contains(director)]
    return filtered_data_bydirector

def load_data_byname(name):
    data = pd.read_csv(doc, index_col=0, encoding='latin-1')
    filtered_data_byname = data[data["name"].str.upper().str.contains(name)]
    return filtered_data_byname

#--- PAGE CONFIG ---#
st.set_page_config(page_title="Netflix App",
                   page_icon=":busts_in_silhouette:")

st.title("Netflix App")

data = load_data(500)

#--- LOGO ---#
st.sidebar.image("cred.jpg")
st.sidebar.write("Adriel Eduardo Peregrina Soto - S20006770")
st.sidebar.markdown("##")
#--- SIDEBAR FILTERS ---#
if st.sidebar.checkbox("Mostras todos los filmes"):
    st.write(data)
    
buscadorTitulo = st.sidebar.write("Titulo del filme")
buscador = st.sidebar.text_input("Titulo filme")
botonTitulo = st.sidebar.button("Buscar filmes")




director = st.sidebar.selectbox("Selecciona el director",
                                options=data['director'].unique())
botonDirector = st.sidebar.button("Buscar por director")


if botonTitulo:
    filterbyname = load_data_byname(buscador.upper())
    rows = filterbyname.shape[0]
    st.dataframe(filterbyname)
    
if botonDirector:
    filterbydirector = load_data_bydirector(director)
    rows = filterbydirector.shape[0]
    st.dataframe(filterbydirector)

    


    