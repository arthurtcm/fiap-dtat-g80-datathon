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
    st.write('Fase: ' + str(aluno.iloc[0]['FASE_' + ano]))
    st.write('Turma: ' + str(aluno.iloc[0]['TURMA_' + ano]))
    st.write('INDE: ' + str(aluno.iloc[0]['INDE_' + ano]))

    st.write('IAA: ' + str(aluno.iloc[0]['IAA_' + ano]))
    st.write('IEG: ' + str(aluno.iloc[0]['IEG_' + ano]))
    st.write('IPS: ' + str(aluno.iloc[0]['IPS_' + ano]))
    st.write('IPP: ' + str(aluno.iloc[0]['IPP_' + ano]))
    st.write('IPV: ' + str(aluno.iloc[0]['IPV_' + ano]))
    st.write('IAN: ' + str(aluno.iloc[0]['IAN_' + ano]))
    st.write('IDA: ' + str(aluno.iloc[0]['IDA_' + ano]))

st.header('Alunos')
st.subheader('Selecione o ano e o aluno ao lado')

st.divider()

ano_selecionado = st.sidebar.selectbox('Escolha o ano', ['2020', '2021', '2022'])
base = carregar_base(ano_selecionado)
aluno_selecionado = st.sidebar.selectbox('Escolha o aluno', base['NOME'].unique())

carregar_info_alunos(aluno_selecionado, ano_selecionado, base)