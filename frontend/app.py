# # import streamlit as st
# # import requests

# # API_URL = "http://localhost:8000/api/administracao/alunos"

# # st.title("Sistema de Alunos")

# # # Listar todos os alunos
# # st.header("Listar Alunos")
# # if st.button("Carregar alunos"):
# #     alunos = requests.get(API_URL).json()
# #     st.table(alunos)

# # # Buscar aluno por ID
# # st.header("Buscar Aluno por ID")
# # aluno_id = st.number_input("ID do aluno", min_value=1, step=1)
# # if st.button("Buscar"):
# #     aluno = requests.get(f"{API_URL}/{aluno_id}").json()
# #     st.json(aluno)

# # # Criar novo aluno
# # st.header("Cadastrar Aluno")
# # with st.form("form_cadastro"):
# #     nome = st.text_input("Nome")
# #     idade = st.number_input("Idade", min_value=0, step=1)
# #     email = st.text_input("Email")
# #     if st.form_submit_button("Cadastrar"):
# #         data = {"nome": nome, "idade": idade, "email": email}
# #         requests.post(API_URL, json=data)
# #         st.success("Aluno cadastrado.")

# # # Atualizar aluno
# # st.header("Atualizar Aluno")
# # with st.form("form_atualizar"):
# #     id_aluno = st.number_input("ID", min_value=1, step=1)
# #     novo_nome = st.text_input("Novo nome")
# #     nova_idade = st.number_input("Nova idade", min_value=0, step=1)
# #     novo_email = st.text_input("Novo email")
# #     if st.form_submit_button("Atualizar"):
# #         data = {"nome": novo_nome, "idade": nova_idade, "email": novo_email}
# #         requests.put(f"{API_URL}/{id_aluno}", json=data)
# #         st.success("Aluno atualizado.")

# # # Deletar aluno
# # st.header("Deletar Aluno")
# # id_delete = st.number_input("ID do aluno", min_value=1, step=1, key="delete")
# # if st.button("Deletar"):
# #     requests.delete(f"{API_URL}/{id_delete}")
# #     st.success("Aluno deletado.")

# import streamlit as st
# import requests

# API_URL = "http://localhost:8000/api/administracao/alunos"

# st.title("Sistema de Alunos")

# # Listar todos os alunos
# st.header("Listar Alunos")
# if st.button("Carregar alunos"):
#     alunos = requests.get(API_URL).json()

#     alunos_formatados = []
#     for a in alunos:
#         alunos_formatados.append({
#             "id": a.get("id"),
#             "nome_aluno": a.get("nome_aluno"),
#             "email": a.get("email") or "",
#             "cep": a.get("cep", {}).get("cep") if a.get("cep") else "",
#             "carro": a.get("carro", {}).get("modelo") if a.get("carro") else "",
#         })

#     st.table(alunos_formatados)

# # Buscar aluno por ID
# st.header("Buscar Aluno por ID")
# aluno_id = st.number_input("ID do aluno", min_value=1, step=1)
# if st.button("Buscar"):
#     aluno = requests.get(f"{API_URL}/{aluno_id}").json()
#     st.json(aluno)

# # Criar novo aluno
# st.header("Cadastrar Aluno")
# with st.form("form_cadastro"):
#     nome = st.text_input("Nome")
#     email = st.text_input("Email")
#     cep = st.text_input("CEP")
#     carro = st.number_input("ID do Carro", min_value=0, step=1)
#     if st.form_submit_button("Cadastrar"):
#         data = {
#             "nome_aluno": nome,
#             "email": email,
#             "cep": cep or None,
#             "carro": carro if carro != 0 else None
#         }
#         requests.post(API_URL, json=data)
#         st.success("Aluno cadastrado.")

# # Atualizar aluno
# st.header("Atualizar Aluno")
# with st.form("form_atualizar"):
#     id_aluno = st.number_input("ID", min_value=1, step=1)
#     novo_nome = st.text_input("Novo nome")
#     novo_email = st.text_input("Novo email")
#     novo_cep = st.text_input("Novo CEP")
#     novo_carro = st.number_input("Novo ID do Carro", min_value=0, step=1)
#     if st.form_submit_button("Atualizar"):
#         data = {
#             "nome_aluno": novo_nome,
#             "email": novo_email,
#             "cep": novo_cep or None,
#             "carro": novo_carro if novo_carro != 0 else None
#         }
#         requests.put(f"{API_URL}/{id_aluno}", json=data)
#         st.success("Aluno atualizado.")

# # Deletar aluno
# st.header("Deletar Aluno")
# id_delete = st.number_input("ID do aluno", min_value=1, step=1, key="delete")
# if st.button("Deletar"):
#     requests.delete(f"{API_URL}/{id_delete}")
#     st.success("Aluno deletado.")


import streamlit as st
import requests

API_URL = "http://localhost:8000/api/administracao/alunos"

st.title("Sistema de Alunos")

# Sidebar para navegação entre as seções
opcao = st.sidebar.selectbox("Menu", [
    "Listar Alunos",
    "Buscar Aluno por ID",
    "Cadastrar Aluno",
    "Atualizar Aluno",
    "Deletar Aluno"
])

if opcao == "Listar Alunos":
    st.header("Listar Alunos")
    if st.button("Carregar alunos"):
        alunos = requests.get(API_URL).json()

        alunos_formatados = []
        for a in alunos:
            alunos_formatados.append({
                "id": a.get("id"),
                "nome_aluno": a.get("nome_aluno"),
                "email": a.get("email") or "",
                "cep": a.get("cep", {}).get("cep") if a.get("cep") else "",
                "carro": a.get("carro", {}).get("modelo") if a.get("carro") else "",
            })

        st.table(alunos_formatados)

elif opcao == "Buscar Aluno por ID":
    st.header("Buscar Aluno por ID")
    aluno_id = st.number_input("ID do aluno", min_value=1, step=1)
    if st.button("Buscar"):
        aluno = requests.get(f"{API_URL}/{aluno_id}").json()
        st.json(aluno)

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
            requests.post(API_URL, json=data)
            st.success("Aluno cadastrado.")

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
            requests.put(f"{API_URL}/{id_aluno}", json=data)
            st.success("Aluno atualizado.")

elif opcao == "Deletar Aluno":
    st.header("Deletar Aluno")
    id_delete = st.number_input("ID do aluno", min_value=1, step=1, key="delete")
    if st.button("Deletar"):
        requests.delete(f"{API_URL}/{id_delete}")
        st.success("Aluno deletado.")
