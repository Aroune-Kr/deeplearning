import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_data():
    data = pd.read_csv('test.csv')
    return data

data = load_data()


st.title('Consommation d’énergies renouvelables par pays')


st.header('Évolution globale de la consommation d’énergies renouvelables')
mean_renewables = data.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], axis=1).mean()
plt.figure(figsize=(10, 5))
plt.plot(mean_renewables.index, mean_renewables.values, marker='o', linestyle='-', color='b')
plt.xticks(rotation=45)
plt.xlabel('Année')
plt.ylabel('% de la consommation totale d\'énergie')
plt.title('Moyenne mondiale de la consommation d’énergies renouvelables')
st.pyplot(plt)


st.header('Comparaison par pays ou région')
selected_countries = st.multiselect('Choisissez les pays à comparer:', data['Country Name'].dropna().unique())
if selected_countries:
    plt.figure(figsize=(10, 5))
    for country in selected_countries:
        country_data = data[data['Country Name'] == country].drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], axis=1).T
        plt.plot(country_data.index, country_data.values, marker='.', label=country)
    plt.xticks(rotation=45)
    plt.legend()
    plt.xlabel('Année')
    plt.ylabel('% de la consommation totale d\'énergie')
    plt.title('Comparaison de la consommation d’énergies renouvelables')
    st.pyplot(plt)


st.header('Répartition de la consommation d’énergies renouvelables en 2000')
data_2020 = data[['Country Name', '2000']].dropna()
plt.figure(figsize=(8, 8))
top_countries = data_2020.sort_values('2000', ascending=False).head(10)
plt.pie(top_countries['2000'], labels=top_countries['Country Name'], autopct='%1.1f%%', startangle=140)
plt.title('Top 10 des pays par consommation d’énergies renouvelables en 2000')
st.pyplot(plt)


