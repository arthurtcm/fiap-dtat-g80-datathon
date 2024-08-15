import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
fig_virada, ax_virada = plt.subplots()
ax_virada.bar(alunos_virada_por_pedra.index, alunos_virada_por_pedra.values, color='skyblue')
ax_virada.set_xlabel('Pedra')
ax_virada.set_ylabel('Total')

if ano_selecionado in ['2022', '2021']:
    alunos_virada_por_fase = total_ponto_virada_por_fase(ano_selecionado, base)
    fig_virada_fase, ax_virada_fase = plt.subplots()
    ax_virada_fase.bar(alunos_virada_por_fase.index, alunos_virada_por_fase.values, color='skyblue')
    ax_virada_fase.set_xlabel('Fase')
    ax_virada_fase.set_ylabel('Total')

st.title('Alunos que atingiram o ponto de virada')
st.pyplot(fig_virada)
if ano_selecionado in ['2022', '2021']:
    st.pyplot(fig_virada_fase)


# PEDRA
total_pedra = base['PEDRA_'+ ano_selecionado].value_counts()
fig, ax = plt.subplots()
ax.pie(total_pedra, labels=total_pedra.index, autopct='%1.1f%%', colors=plt.cm.Paired(np.arange(len(total_pedra))))

st.title('Distribuição de alunos por PEDRAS')
st.pyplot(fig)

#Total de Alunos recomendados para um nivel maior que o atual

if ano_selecionado in ['2022', '2021']:
    total_upgrade_por_pedra = total_upgrade_por_pedra(ano_selecionado, base)
    
    fig_upgrade, ax_upgrade = plt.subplots()
    ax_upgrade.bar(total_upgrade_por_pedra.index, total_upgrade_por_pedra.values, color='skyblue')
    ax_upgrade.set_xlabel('Pedra')
    ax_upgrade.set_ylabel('Total')

    st.title('Total de Alunos recomendados para um nivel maior que o atual')
    st.pyplot(fig_upgrade)





