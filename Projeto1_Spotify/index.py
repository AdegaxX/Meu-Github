import pandas as pd
import kagglehub

path = kagglehub.dataset_download("asmonline/spotify-song-performance-dataset")
print("Path to dataset files:", path)
# Carregando e explorando os dados:
pasta = path + '/spotify_song_performace.csv'

df = pd.read_csv(pasta) # Lê o arquivo .csv

print(df.head())        # Inspeciona as primeiras linhas
print(df.info())        # Informações gerais sobre coluna e tipos de dados
print(df.describe())    # Resumo estatístico
