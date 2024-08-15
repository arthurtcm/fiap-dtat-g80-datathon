import streamlit as st
import pandas as pd
import numpy as np


@st.cache_data
def carregar_base(ano):
    caminho_base = 'bases/base_' + ano + '.csv'
    base = pd.read_csv(caminho_base, sep =',')
    return base

def total_upgrade_por_pedra(ano, base):
    df_upgrade = base[base['FASE_' + ano] < base['NIVEL_IDEAL_' + ano + '_NUM']]

    total = df_upgrade['PEDRA_' + ano].value_counts()

    return total


ano_selecionado = st.selectbox('Escolha o ano', ['2020', '2021', '2022'])
base = carregar_base(ano_selecionado)


total_upgrade_por_pedra = total_upgrade_por_pedra(ano_selecionado, base)
st.title('Total de Alunos recomendados para um nivel maior que o atual')
st.bar_chart(total_upgrade_por_pedra)