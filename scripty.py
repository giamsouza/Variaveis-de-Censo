import pandas as pd

# Carregar o DataFrame a partir de um arquivo CSV
census_dataframe = pd.read_csv('census_data.csv')  # Substitua pelo caminho correto do seu arquivo CSV

# Verificar as colunas no DataFrame
print(census_dataframe.columns)  # Verifique o nome da coluna de estado civil

# 1. Visualizar as cinco primeiras linhas
print(census_dataframe.head())  

# 2. Revisar a descrição do DataFrame e os tipos de variáveis
print(census_dataframe.describe())  
print(census_dataframe.dtypes)  

# 3. Inspecionar os tipos de dados
print(census_dataframe.dtypes)

# 4. Verificar os valores únicos da coluna birth_year
print(census_dataframe['birth_year'].unique())

# 5. Substituir valores faltantes na coluna birth_year
census_dataframe['birth_year'] = census_dataframe['birth_year'].replace('missing', '1967')
print(census_dataframe['birth_year'].unique())

# 6. Converter birth_year para inteiro
census_dataframe['birth_year'] = census_dataframe['birth_year'].astype(int)
print(census_dataframe.dtypes)

# 7. Calcular o ano médio de nascimento
year_mean = census_dataframe['birth_year'].mean()
print("Ano médio de nascimento:", year_mean)

# 8. Ordenar higher_tax como categoria ordenada
order = ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree']
census_dataframe['higher_tax'] = pd.Categorical(census_dataframe['higher_tax'], categories=order, ordered=True)
print(census_dataframe['higher_tax'].unique())

# 9. Codificar higher_tax e calcular a mediana
census_dataframe['higher_tax_code'] = census_dataframe['higher_tax'].cat.codes
median_tax = census_dataframe['higher_tax_code'].median()
print("Mediana de higher_tax:", median_tax)

# 10. One-Hot Encoding para marital_status (verifique se o nome da coluna está correto)
census_dataframe = pd.get_dummies(census_dataframe, columns=['marital_status'])  # Substitua 'marital_status' pelo nome correto da coluna, se necessário
print(census_dataframe.head())  # Mostrar as 5 primeiras linhas do DataFrame com One-Hot Encoding

# 11. Criar uma variável de Label Encoding para marital_status (certifique-se de usar o nome correto da coluna)
census_dataframe['marital_codes'] = census_dataframe['marital_status'].astype('category').cat.codes  # Substitua 'marital_status' pelo nome correto

# Criar age_group e codificar
bins = list(range(census_dataframe['birth_year'].min(), census_dataframe['birth_year'].max(), 5))
labels = [f"{b}-{b+4}" for b in bins[:-1]]
census_dataframe['age_group'] = pd.cut(census_dataframe['birth_year'], bins=bins, labels=labels, right=False)
census_dataframe['age_group_code'] = census_dataframe['age_group'].astype('category').cat.codes

print(census_dataframe.head())  # Exibir as 5 primeiras linhas após a transformação

