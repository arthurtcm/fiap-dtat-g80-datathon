import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def carregar_base(ano):
    caminho_base = 'bases/base_' + ano + '.csv'
    base = pd.read_csv(caminho_base, sep =',')
    return base

def total_ponto_virada_por_pedra(ano, base):
    df_virada_sim = base[base['PONTO_VIRADA_' + ano] == 'Sim']

    total = df_virada_sim['PEDRA_' + ano].value_counts()

    return total

def total_ponto_virada_por_fase(ano, base):
    df_virada_sim = base[base['PONTO_VIRADA_' + ano] == 'Sim']

    total = df_virada_sim['FASE_' + ano].value_counts()
    total.index = total.index.astype(int)
    total = total.sort_index()

    return total


def total_upgrade_por_pedra(ano, base):
    df_upgrade = base[base['FASE_' + ano] < base['NIVEL_IDEAL_' + ano + '_NUM']]

    total = df_upgrade['PEDRA_' + ano].value_counts()

    return total



st.title('Datathon')


ano_selecionado = st.sidebar.selectbox('Escolha o ano', ['2020', '2021', '2022'])

base = carregar_base(ano_selecionado)

st.write(base.head())

#VIRADA POR PEDRA

alunos_virada_por_pedra = total_ponto_virada_por_pedra(ano_selecionado, base)
st.title('Alunos que atingiram o ponto de virada por pedra')
st.bar_chart(alunos_virada_por_pedra)

if ano_selecionado in ['2022', '2021']:
    alunos_virada_por_fase = total_ponto_virada_por_fase(ano_selecionado, base)
    st.title('Alunos que atingiram o ponto de virada por fase')
    st.bar_chart(alunos_virada_por_fase)


#Total de Alunos recomendados para um nivel maior que o atual

if ano_selecionado in ['2022', '2021']:
    total_upgrade_por_pedra = total_upgrade_por_pedra(ano_selecionado, base)
    st.title('Total de Alunos recomendados para um nivel maior que o atual')
    st.bar_chart(total_upgrade_por_pedra)