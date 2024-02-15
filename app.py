import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
@st.cache
def load_data():
    df = pd.read_csv('games.csv')
    return df

df = load_data()

# Página principal
def main():
    st.title('Análise de Dados de Games')

    # Sidebar para filtros e configurações
    st.sidebar.title('Configurações')
    genre_filter = st.sidebar.multiselect('Filtrar por Gênero:', df['genre'].unique())
    platform_filter = st.sidebar.multiselect('Filtrar por Plataforma:', df['platform'].unique())

    # Aplicar filtros
    filtered_df = df[df['genre'].isin(genre_filter) & df['platform'].isin(platform_filter)]

    # Visão Geral dos Dados
    st.write('## Visão Geral dos Dados')
    st.write(filtered_df.head())

    # Gráfico de Barras das Vendas por Plataforma
    st.write('## Gráfico de Barras das Vendas por Plataforma')
    sales_by_platform = filtered_df.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_platform)

    # Diagrama de Caixa das Vendas Globais por Gênero
    st.write('## Diagrama de Caixa das Vendas Globais por Gênero')
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=filtered_df, x='genre', y='total_sales')
    plt.xticks(rotation=45)
    st.pyplot()