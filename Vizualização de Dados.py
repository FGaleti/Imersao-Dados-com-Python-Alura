import pandas as pd 
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
# df.head()
# df.info()
# df.describe()
# df.shape
# linhas, colunas = df.shape[0], df.shape[1]
# print(f"O dataset possui {linhas} linhas e {colunas} colunas.")
# df.columns

# traducao_colunas = {
#     'work_year': 'ano_de_trabalho',
#     'experience_level': 'nivel_de_experiencia',
#     'employment_type': 'tipo_de_emprego',
#     'job_title': 'titulo_do_trabalho',
#     'salary': 'salario',
#     'salary_currency': 'moeda_do_salario',
#     'salary_in_usd': 'salario_em_usd',
#     'employee_residence': 'residencia_do_funcionario',
#     'remote_ratio': 'proporcao_remota',
#     'company_location': 'localizacao_da_empresa',
#     'company_size': 'tamanho_da_empresa'
# }

# df.rename(columns=traducao_colunas, inplace=True)
# print("Colunas traduzidas:", df.columns)

# df['nivel_de_experiencia'].value_counts()

# df['nivel_de_experiencia'].value_counts(normalize=True) * 100

# df.head()
# df. describe(include='object')

# df.isnull().sum()
# df['ano_de_trabalho'].unique()
# df[df.isnull().any(axis=1)]

import numpy as np
import matplotlib.pyplot as plt

df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'salario': [5000, np.nan, 7000, np.nan],  
})


media_salario = df_salarios['salario'].mean()
df_salarios['salario'].fillna(media_salario, inplace=True)
df_salarios['salario_medio'] = media_salario
print("DataFrame de Salários (preenchido com média):")
print(df_salarios)

df_temperaturas = pd.DataFrame({
    "Dia": ['segunda', 'terca', 'quarta', 'quinta', 'sexta'],
    "Temperatura": [22, 21, np.nan, 24, np.nan]
})

df_temperaturas['Temperatura'].interpolate(method='linear', inplace=True)
print("\nDataFrame de Temperaturas (interpoladas):")
print(df_temperaturas)

df_cidades = pd.DataFrame({
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador'],
    'População': [12300000, np.nan, 2520000, np.nan, 2880000],
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva'],
})

df_cidades['População'].ffill(inplace=True)
print("\nDataFrame de Cidades (forward fill):")
print(df_cidades)

df_limpo = df.dropna()


print("\nValidação de valores nulos após limpeza:")
print(df_limpo.isnull().sum())

print("\nPrimeiras linhas do dataset limpo:")
print(df_limpo.head())

print("\nInformações do dataset limpo:")
print(df_limpo.info())

df_limpo['work_year'] = df_limpo['work_year'].astype(int)


if 'experience_level' in df_limpo.columns:
    df_limpo['experience_level'].value_counts().plot(kind='bar', title='Distribuição de Nível de Experiência', figsize=(10, 6))
    plt.xlabel('Nível de Experiência')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    plt.show()
else:
    print("Aviso: Coluna 'experience_level' não encontrada no dataset.")

import seaborn as sns

#sns.barplot(x='experience_level', y='salary_in_usd', data=df_limpo)
#plt.title('Salário Médio por Nível de Experiência')
#plt.xlabel('Nível de Experiência')
#plt.ylabel('Salário em USD')
#plt.tight_layout()
#plt.show()

import matplotlib.pyplot as plt

#plt.figure(figsize=(10, 6))
#plt.hist(df_limpo['salary_in_usd'], bins=30, color='skyblue', edgecolor='black')
#plt.title('Distribuição de Salários em USD')
#plt.xlabel('Nível de Experiência')
#plt.ylabel('Salário em USD')
#plt.tight_layout()
#plt.show()

df_limpo.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False).plot(kind='bar', title='Salário Médio por Nível de Experiência', figsize=(10, 6))
ordem = df_limpo.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False).index
plt.xlabel('Nível de Experiência')
plt.ylabel('Salário Médio em USD')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df_limpo['salary_in_usd'], bins=50, kde=True, color='skyblue') 
plt.title('Distribuição de Salários em USD')
plt.xlabel('Salário em USD')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
ordem_senioridade = ['EN', 'MI', 'SE', 'EX']
sns.boxplot(x='experience_level', y='salary_in_usd', data=df_limpo, order=ordem_senioridade)
plt.title('Salário em USD por Nível de Experiência')
plt.xlabel('Nível de Experiência')
plt.ylabel('Salário em USD')
plt.tight_layout()
plt.show()

import plotly.express as px
# Interativo
fig = px.bar(df_limpo.groupby('experience_level')['salary_in_usd'].mean().reset_index(),
             x='experience_level',
             y='salary_in_usd',
                title='Salário Médio por Nível de Experiência',
                labels={'experience_level': 'Nível de Experiência', 'salary_in_usd': 'Salário Médio em USD'})
fig.show()

remoto_contagem = df_limpo['remote_ratio'].value_counts().reset_index()
remoto_contagem.columns = ['remote_ratio', 'contagem']
fig = px.pie(remoto_contagem, values='contagem', names='remote_ratio',
             title='Proporção de Trabalho Remoto')
fig.show()

remoto_contagem = df_limpo['remote_ratio'].value_counts().reset_index()
remoto_contagem.columns = ['remote_ratio', 'contagem']
fig = px.pie(remoto_contagem, values='contagem', names='remote_ratio',
             title='Proporção de Trabalho Remoto',
             hole=0.5)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

