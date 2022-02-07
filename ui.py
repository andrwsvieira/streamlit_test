from unicodedata import decimal
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt


st.write("""
# Top Provedores de Internet
By *ANATEL*
""")

df = pd.read_csv('Relatorio_Provedores_Anatel.csv', sep= ';', decimal=',')

a = df.head()


st.dataframe(a)