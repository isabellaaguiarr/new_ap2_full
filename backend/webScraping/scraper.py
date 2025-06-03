import asyncio
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings

async def coletar_dados():
    options = Options()
    url = 'https://www.dfimoveis.com.br/'
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # Parâmetros de pesquisa
    tipo = "VENDA"
    tipos = "CASA"
    estado = "DF"
    cidade = "GUARA"
    quartos = "2"

    # Preenche os filtros na página
    async def preencher_filtro(by, value, texto):
        element = wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
        search_field = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-search__field")))
        search_field.send_keys(texto)
        search_field.send_keys(Keys.ENTER)

    await preencher_filtro(By.ID, 'select2-negocios-container', tipo)
    await preencher_filtro(By.ID, 'select2-tipos-container', tipos)
    await preencher_filtro(By.ID, 'select2-estados-container', estado)
    await preencher_filtro(By.ID, 'select2-cidades-container', cidade)
    

    # Seleção de quartos
    element = wait.until(EC.element_to_be_clickable((By.ID, 'select2-quartos-container')))
    element.click()

    opcoesQuartos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'select2-results__option')))
    for opcao in opcoesQuartos:
        if opcao.text.strip() == quartos:
            opcao.click()
            break

    # Busca os imóveis
    busca = wait.until(EC.element_to_be_clickable((By.ID, "botaoDeBusca")))
    busca.click()

    lst_imoveis = []
    while True:
        resultado = wait.until(EC.presence_of_element_located((By.ID, "resultadoDaBuscaDeImoveis")))
        elementos = resultado.find_elements(By.TAG_NAME, 'a')

        for elem in elementos:
            imovel = {
                'titulo': elem.find_element(By.CLASS_NAME, 'new-title').text,
                'preco': elem.find_element(By.CLASS_NAME, 'new-price').text,
                'metragem': elem.find_element(By.CLASS_NAME, 'm-area').text,
                'quarto': quartos,
                'descricao': elem.find_element(By.CLASS_NAME, 'new-text').text
            }
            lst_imoveis.append(imovel)

        botao_proximo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.next')))
        if botao_proximo.get_attribute("class") == "btn disabled next":
            break

        driver.execute_script("arguments[0].click();", botao_proximo)
        await asyncio.sleep(2)  # Espera assíncrona

    driver.quit()
    
    # Obtém as configurações do banco de dados a partir do settings.py
    db_config = settings.DATABASES['db_imoveis']
    DATABASE_URL = f"mysql+pymysql://{db_config['USER']}:{db_config['PASSWORD']}@{db_config['HOST']}:{db_config['PORT']}/{db_config['NAME']}"
    
    # Limpeza e retorno dos dados coletados
    df = pd.DataFrame(lst_imoveis)
    df["preco"] = df["preco"].apply(lambda x: x.split("\n")[0].replace("R$", "").replace(".", "").strip())
    df["metragem"] = df["metragem"].apply(lambda x: x.replace("m²", "").strip())

    # Salvar no banco
    engine = create_engine(DATABASE_URL)
    df.to_sql('tb_imoveis', con=engine, if_exists='append', index=False)

    print("Dados coletados e inseridos no banco!")

    return df.to_dict(orient="records")  # Retorna os dados coletados




