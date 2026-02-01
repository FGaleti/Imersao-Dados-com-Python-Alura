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
df_salarios = pd.DataFrame({
    'nome' : ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'salario' : [5000, np.nan, 7000, np.nan],  
})
df_salarios['salrio_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean())
df_salarios['salario'].fillna(df_salarios['salario'].mean(), inplace=True)
print(df_salarios)

df_temperaturas = pd.DataFrame({
    "Dia" : ['segunda', 'terca', 'quarta', 'quinta', 'sexta'],
    "Temperatura" : [22, 21, np.nan, 24, np.nan]
})

df_temperaturas['Temperatura'].interpolate(method='linear', inplace=True)
print(df_temperaturas)

df_cidades = pd.DataFrame({
    'Cidade' : ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador'],
    'População' : [12300000, np.nan, 2520000, np.nan, 2880000],
    'nome' : ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva'],
})
df_cidades['Cidade'] = df_cidades['Cidade'].fillna(method='ffill')
print(df_cidades)


df_limpo = df.dropna()
df_limpo.isnull().sum()
df_limpo.head()
df_limpo.info()
print(df_limpo)

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype(int))



