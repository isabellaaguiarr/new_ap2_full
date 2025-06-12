import streamlit as st
import requests
import pandas as pd
import time

API_URL = "http://localhost:8000/api/administracao/alunos"
SCRAPING_URL = "http://127.0.0.1:8000/scrape/"
DADOS_URL = "http://127.0.0.1:8000/obter_dados/"

st.title("Sistema de Gerenciamento")

# Barra lateral 
opcao = st.sidebar.selectbox("Menu", [
    "Listar Alunos",
    "Buscar Aluno por ID",
    "Cadastrar Aluno",
    "Atualizar Aluno",
    "Deletar Aluno",
    "Iniciar Web Scraping"
])

# Listar Alunos
if opcao == "Listar Alunos":
    st.header("Lista de Alunos")
    if st.button("Carregar alunos"):
        response = requests.get(API_URL)
        if response.status_code == 200:
            alunos = response.json()
            df_alunos = pd.DataFrame(alunos)
            st.dataframe(df_alunos, height=400, width=1000)  #
        else:
            st.error("Erro ao buscar alunos. Verifique a API.")

# Buscar Alunos
elif opcao == "Buscar Aluno por ID":
    st.header("Buscar Aluno por ID")
    aluno_id = st.number_input("ID do aluno", min_value=1, step=1)
    if st.button("Buscar"):
        response = requests.get(f"{API_URL}/{aluno_id}")
        if response.status_code == 200:
            aluno = response.json()
            # Convertendo para DataFrame
            df_aluno = pd.DataFrame([aluno])
            st.dataframe(df_aluno)
        else:
            st.error("Aluno não encontrado.")

# Cadastrar Alunos
elif opcao == "Cadastrar Aluno":
    st.header("Cadastrar Aluno")
    with st.form("form_cadastro"):
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        cep = st.text_input("CEP")
        carro = st.number_input("ID do Carro", min_value=0, step=1)
        if st.form_submit_button("Cadastrar"):
            data = {
                "nome_aluno": nome,
                "email": email,
                "cep": cep or None,
                "carro": carro if carro != 0 else None
            }
            response = requests.post(API_URL, json=data)
            if response.status_code == 201:
                st.success("Aluno cadastrado com sucesso.")
            else:
                st.error("Erro ao cadastrar aluno.")

# Atualizar Alunos
elif opcao == "Atualizar Aluno":
    st.header("Atualizar Aluno")
    with st.form("form_atualizar"):
        id_aluno = st.number_input("ID", min_value=1, step=1)
        novo_nome = st.text_input("Novo nome")
        novo_email = st.text_input("Novo email")
        novo_cep = st.text_input("Novo CEP")
        novo_carro = st.number_input("Novo ID do Carro", min_value=0, step=1)
        if st.form_submit_button("Atualizar"):
            data = {
                "nome_aluno": novo_nome,
                "email": novo_email,
                "cep": novo_cep or None,
                "carro": novo_carro if novo_carro != 0 else None
            }
            response = requests.put(f"{API_URL}/{id_aluno}", json=data)
            if response.status_code == 200:
                st.success("Aluno atualizado com sucesso.")
            else:
                st.error("Erro ao atualizar aluno.")

# Deletar Alunos
elif opcao == "Deletar Aluno":
    st.header("Deletar Aluno")
    id_delete = st.number_input("ID do aluno", min_value=1, step=1, key="delete")
    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/{id_delete}")
        if response.status_code == 204:
            st.success("Aluno deletado com sucesso.")
        else:
            st.error("Erro ao deletar aluno.")

# WebScraping 
elif opcao == "Iniciar Web Scraping":
    st.header("Iniciar Web Scraping")
    if st.button("Executar Scraping"):
        with st.spinner("Executando scraping... Aguarde!"):
            response = requests.get(SCRAPING_URL)

        if response.status_code == 200:
            st.success("Scraping iniciado com sucesso! Aguardando a coleta de dados...")

            # Aguarda um tempo para garantir que os dados sejam processados no backend
            time.sleep(10)

            # Faz a requisição para obter os dados coletados após o scraping
            response_dados = requests.get(DADOS_URL)
            if response_dados.status_code == 200:
                json_data = response_dados.json()
                st.success("Dados coletados com sucesso!")

            else:
                st.error(f"Erro ao buscar os dados coletados: Código {response_dados.status_code}")
        else:
            st.error(f"Erro ao iniciar o scraping: Código {response.status_code}")
