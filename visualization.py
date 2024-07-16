import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

st.title(' streamlit app')
st.header('Welcome')
file = st.file_uploader('importer le fichier')
if file is not None:
    df = load_data(file)
    nombre_lignes = st.slider('choisir nombre des lignes a afficher:', min_value=2, max_value=len(df))
    colonnes = st.multiselect('selectionner les colonnes a afficher:', options=df.columns.to_list(), default=df.columns.to_list())
    st.write(df[:nombre_lignes][colonnes])
    
    colonnes_num = df.select_dtypes(include=np.number).columns.to_list()
        
    tab1, tab2 = st.tabs(['Scatter Plot', 'Histogram'])
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            x_col = st.selectbox('choisir la caracteristique sur axe x:', colonnes_num)
        with col2:
            y_col = st.selectbox('choisir la caracteristique sur axe y:', colonnes_num)
        with col3:
            color = st.selectbox('choisir la caracteristique color:', df.columns)
        fig_scatter = px.scatter(df, x_col, y_col, color=color)
        st.plotly_chart(fig_scatter)
    with tab2:
        feat = st.selectbox('choisir la caracteristique:', colonnes_num)
        fig_hist = px.histogram(df, x=feat)
        st.plotly_chart(fig_hist)

