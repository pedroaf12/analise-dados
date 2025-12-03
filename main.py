import pandas as pd
from pandasgui import show

tabela = pd.read_csv("./database/ClientesBanco.csv", sep=",", encoding="latin1")

# Tratando valores vazios e exibindo resumo das colunas da base de dados
tabela = tabela.drop("CLIENTNUM", axis=1)
tabela = tabela.dropna()
# show(tabela.describe().round(1))


# Avaliando divisão entre clientes x cancelados
qtd_categoria = tabela["Categoria"].value_counts()
print(qtd_categoria)
percentual = tabela["Categoria"].value_counts(normalize=True)
print(percentual)
