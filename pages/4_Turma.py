import streamlit as st
import pandas as pd
import numpy as np


@st.cache_data
def carregar_base(ano):
    caminho_base = 'bases/base_' + ano + '.csv'
    base = pd.read_csv(caminho_base, sep =',')
    return base

def pedras_por_turma(ano, turma, base):
    df_turma = base[base['TURMA_' + ano] == turma]

    total = df_turma['PEDRA_' + ano].value_counts()

    st.write('# Total de alunos de cada pedra')
    st.bar_chart(total)


def total_alunos(ano, turma, base):
    total = (base['TURMA_' + ano] == turma).sum()

    st.write('Total de alunos: ' + str(total))

def total_virada(ano, turma, base):
    df_turma = base[base['TURMA_' + ano] == turma]
    total = (df_turma['PONTO_VIRADA_' + ano] == 'Sim').sum()

    st.write('Total de alunos da turma que atingiram o ponto de virada: ' + str(total))

st.header('Turma')
st.subheader('Selecione o ano e a turma ao lado')

st.divider()

ano_selecionado = st.sidebar.selectbox('Escolha o ano', ['2020', '2021', '2022'])
base = carregar_base(ano_selecionado)
turma_selecionada = st.sidebar.selectbox('Escolha a turma', base['TURMA_' + ano_selecionado].unique())

st.write('Turma: ' + turma_selecionada)
st.write('Ano: ' + ano_selecionado)

st.divider()
total_alunos(ano_selecionado, turma_selecionada, base)
total_virada(ano_selecionado, turma_selecionada, base)
pedras_por_turma(ano_selecionado, turma_selecionada, base)

