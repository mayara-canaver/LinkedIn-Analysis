import warnings
import pandas as pd

warnings.simplefilter("ignore")
pd.options.display.max_columns = None


# FUNÇÃO QUE ALTERA OS NOMES DE CARGOS ANTERIORES PARA UM GRUPO GERAL
def altera_cargo(cargo_antigo, cargo_atual):
    conexao.loc[(conexao["POSITION"].str.contains(cargo_antigo)), "POSITION"] = cargo_atual

# CAMINHO DOS DATASETS UTILIZADOS
conexao = pd.read_csv("C:/Users/Mayara Lopes/Desktop/Connections.csv")
certificacao = pd.read_csv("C:/Users/Mayara Lopes/Desktop/Certifications.csv")
skill = pd.read_csv("C:/Users/Mayara Lopes/Desktop/Skills.csv", sep=";")
causes = pd.read_csv("C:/Users/Mayara Lopes/Desktop/Causes You Care About.csv", sep=";")
endorsement = pd.read_csv("C:/Users/Mayara Lopes/Desktop/Endorsement_Received_Info.csv")

lista_arquivos = [conexao, certificacao, skill, causes, endorsement]

for arquivo in lista_arquivos:
    arquivo.columns = arquivo.columns.str.upper()

    for coluna in arquivo:
        arquivo[coluna] = arquivo[coluna].astype(str).str.upper()


# CRIANDO UM DICIONÁRIOS DE CARGOS E GRUPOS
dic_cargos = {
    "CIENTISTA DE DADOS": "CIENTISTA DE DADOS|DATA SCIENTIST|DATA SCIENCE",
    "ANALISTA DE DADOS": "ANALISTA DE DADOS|ANÁLISE DE DADOS|DATA ANALYST",
    "ENGENHEIRO DE DADOS": "ENGENHEIRO DE DADOS|DATA ENGINEER",
    "ESTATÍSTICO": "ESTATÍSTICO|ESTATISTA",
    "ANALISTA DE BI": "ANALISTA DE BI",
    "DEV FRONT END": "FRONT-END|FRONT END|DESENVOLVEDOR WEB|WEB DEVELOPMENT",
    "DEV BACK END": "BACKEND|BACK END|BACK-END",
    "DEV FULL STACK": "FULL-STACK|FULL STACK|FULLSTACK",
    "DESENVOLVEDOR": "PROGRAMADOR|DESENVOLVEDOR",
    "ESTAGIÁRIO": "ESTAGIÁRIO|ESTÁGIO|ESTAGIO",
    "SUPORTE": "HELPDESK|SUPORTE|CUSTOMER SUCCESS",
    "MACHINE LEARNING ENGINEER": "MACHINE LEARNING ENGINEER",
    "PROFESSOR": "PROFESSOR|PROF",
    "ESTUDANTE": "ESTUDANTE|STUDENT"
}

# ALTERAÇÃO DOS CARGOS PARA CRIAR UM GRUPO DE CARGOS EM COMUM
for grupo, valor in dic_cargos.items():
    altera_cargo(valor, grupo)

# REMOÇÃO DE CARGOS NAN
conexao = conexao[~conexao["POSITION"].str.contains("NAN")]

for arquivo in lista_arquivos:
    conexao.to_csv(r"C:/Users/Mayara Lopes/Desktop/" + arquivo + ".csv", index=False)
