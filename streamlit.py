import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def carregar_base():
    base = pd.read_csv('bases/base_2022.csv', sep =',')
    return base


st.title('Datathon')

base = carregar_base()

st.write(base.head())
