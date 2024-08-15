import streamlit as st
import pandas as pd
import numpy as np


@st.cache_data
def carregar_base(ano):
    caminho_base = 'bases/base_' + ano + '.csv'
    base = pd.read_csv(caminho_base, sep =',')
    return base

def carregar_info_alunos(nome, ano, base):
    aluno = base.loc[base['NOME'] == nome]

    st.write('Nome: ' + str(aluno.iloc[0]['NOME']))
    st.write('Pedra: ' + str(aluno.iloc[0]['PEDRA_' + ano]))
    st.write('INDE: ' + str(aluno.iloc[0]['INDE_' + ano]))
    st.write('Fase: ' + str(aluno.iloc[0]['FASE_' + ano]))
    st.write('Turma: ' + str(aluno.iloc[0]['TURMA_' + ano]))


ano_selecionado = st.selectbox('Escolha o ano', ['2020', '2021', '2022'])
base = carregar_base(ano_selecionado)
aluno_selecionado = st.selectbox('Escolha o aluno', base['NOME'].unique())

carregar_info_alunos(aluno_selecionado, ano_selecionado, base)