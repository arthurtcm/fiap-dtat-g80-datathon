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

def perc_ponto_virada_por_pedra(ano, base):
    total_por_pedra = base.groupby('PEDRA_' + ano).size()
    total_sim_por_pedra = base[base['PONTO_VIRADA_' + ano] == 'Sim'].groupby('PEDRA_' + ano).size()

    percentuais = (total_sim_por_pedra / total_por_pedra * 100).fillna(0)

    return percentuais

def perc_ponto_virada_por_fase(ano, base):
    total_por_fase = base.groupby('FASE_' + ano).size()
    total_sim_por_fase = base[base['PONTO_VIRADA_' + ano] == 'Sim'].groupby('FASE_' + ano).size()

    percentuais = (total_sim_por_fase / total_por_fase * 100).fillna(0)

    return percentuais


st.header('Ponto de Virada')
st.subheader('Selecione o ano ao lado')

st.divider()

ano_selecionado = st.sidebar.selectbox('Escolha o ano', ['2020', '2021', '2022'])
base = carregar_base(ano_selecionado)

alunos_virada_por_pedra = total_ponto_virada_por_pedra(ano_selecionado, base)
st.title('Total de alunos que atingiram o ponto de virada por pedra')
st.bar_chart(alunos_virada_por_pedra)


alunos_virada_por_fase = total_ponto_virada_por_fase(ano_selecionado, base)
st.title('Total de alunos que atingiram o ponto de virada por fase')
st.bar_chart(alunos_virada_por_fase)

perc_virada_por_pedra = perc_ponto_virada_por_pedra(ano_selecionado, base)
st.title('Percentual de alunos que atingiram o ponto de virada por pedra')
st.bar_chart(perc_virada_por_pedra)

perc_virada_por_fase = perc_ponto_virada_por_fase(ano_selecionado, base)
st.title('Percentual de alunos que atingiram o ponto de virada por fase')
st.bar_chart(perc_virada_por_fase)