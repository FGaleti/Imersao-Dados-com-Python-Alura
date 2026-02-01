import pandas as pd 
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
df.head()
df.info()
df.describe()
df.shape
linhas, colunas = df.shape[0], df.shape[1]
print(f"O dataset possui {linhas} linhas e {colunas} colunas.")
df.columns

traducao_colunas = {
    'work_year': 'ano_de_trabalho',
    'experience_level': 'nivel_de_experiencia',
    'employment_type': 'tipo_de_emprego',
    'job_title': 'titulo_do_trabalho',
    'salary': 'salario',
    'salary_currency': 'moeda_do_salario',
    'salary_in_usd': 'salario_em_usd',
    'employee_residence': 'residencia_do_funcionario',
    'remote_ratio': 'proporcao_remota',
    'company_location': 'localizacao_da_empresa',
    'company_size': 'tamanho_da_empresa'
}

df.rename(columns=traducao_colunas, inplace=True)
print("Colunas traduzidas:", df.columns)

df['nivel_de_experiencia'].value_counts()

df['nivel_de_experiencia'].value_counts(normalize=True) * 100

df.head()
df. describe(include='object')








