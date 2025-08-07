import streamlit as st
import pandas as pd
import plotly.express as px # Boa para gráficos interativos no Streamlit

# Cabeçalho do aplicativo
st.header('Dashboard de Anúncios de Veículos')

# Carregar dados (assumindo que vehicles_us.csv está na mesma pasta)
df = pd.read_csv('vehicles.csv')

# Exemplo simples de EDA no app (você pode expandir)
st.write("Visão geral dos dados:")
st.write(df.head())

# Criar um histograma (Exemplo: por ano do modelo)
st.subheader('Distribuição de Ano do Modelo')
fig_hist = px.histogram(df, x='model_year', title='Histograma do Ano do Modelo')
st.plotly_chart(fig_hist)

# Criar um gráfico de dispersão (Exemplo: preço vs. odômetro)
st.subheader('Preço vs. Odômetro')
fig_scatter = px.scatter(df, x='odometer', y='price', title='Preço vs. Odômetro')
st.plotly_chart(fig_scatter)

# Adicione mais gráficos e interatividade conforme o seu projeto pedir