import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')

st.header('Análise de Anúncios de Vendas de Carros')

# Criar um checkbox para o histograma
hist_checkbox = st.checkbox('Criar um histograma de preços')
#Ao selecionar o checkbox de histograma
if hist_checkbox: 
    st.write('Criando um histograma para o preço dos anúncios de vendas de carros')

    fig = px.histogram(car_data, x="price", nbins=50, title='Distribuição de Preços')

    st.plotly_chart(fig, use_container_width=True)

# Criar um checkbox para o gráfico de dispersão
scatter_checkbox = st.checkbox('Criar um gráfico de dispersão: preço vs. odômetro')
#Ao selecionar o checkbox de grafico de dispersão
if scatter_checkbox: 
    st.write('Criando um gráfico de dispersão para preço e odômetro')

    fig = px.scatter(car_data, x="odometer", y="price", title='Relação entre Preço e Odômetro')

    st.plotly_chart(fig, use_container_width=True)
