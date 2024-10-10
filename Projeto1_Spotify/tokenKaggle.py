import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Defina o caminho do arquivo kaggle.json
os.environ['KAGGLE_CONFIG_DIR'] = "C:/Adegax/Ciência de dados - UFC/Meu Github/Projeto1_Spotify/kaggle.json"  # Substitua pelo caminho correto

# Autenticação no Kaggle
api = KaggleApi()
api.authenticate()

# Baixar o dataset
dataset = "asmonline/spotify-song-performance-dataset"
api.dataset_download_files(dataset, path='./spotify_data', unzip=True)

print("Dataset baixado e extraído no diretório './spotify_data'")
