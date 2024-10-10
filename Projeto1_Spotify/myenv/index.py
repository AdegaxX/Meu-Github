''' Lista de músicas mais tocadas de 2024:   '''

# Importações:
import pandas as pd                 # Tratar dados
import matplotlib.pyplot as plt     # Plotar gráficos
import seaborn as sns

# Explorando e importanto os dados:
df = pd.read_csv("Projeto1_Spotify\\spotify_data.csv") # Lê o arquivo .csv

print(df.head())                   # Inspeciona as primeiras linhas
print(df.info())                   # Informações gerais sobre coluna e tipos de dados
print(df.describe())               # Resumo estatístico

# Tratando os dados:
print(df.isnull().sum())            # Valores ausentes
df.fillna(0, inplace=True)          # Preenche os valores nulos com 0
df.drop_duplicates(inplace=True)    # Remove duplicadas se possuir
df.hist(bins=20, figsize=(15,10))
plt.show()

