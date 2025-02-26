import pandas as pd

df = pd.read_csv('filmes.csv')

print (df.head())

filmes_bons = df[df['nota'] > 8]

filmes_bons.to_csv('filmes_bons.csv', index=False)

print ("Arquivo filmes_bons.csv salvo com sucesso!")
