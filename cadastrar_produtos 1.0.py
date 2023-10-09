import requests
import json
from requests import request
import random


#NOTE - Credenciais
app_key = "apy key base omie"
app_secret = "apy secret base omie"
endpoint_incluir_produtos = "https://app.omie.com.br/api/v1/geral/produtos/"
endpoint_listar_familias = "https://app.omie.com.br/api/v1/geral/familias/"

#NOTE - Anota ai
Authorization = "Authorization sistema anota ai"

#NOTE - Variáveis
ncm_insumos = '2106.90.90'
ncm_refrigerantes = '2202.10.00'
ncm_cerveja = '2203.00.00'
ncm_porcoes = '1905.90.90'
ncm_pizza = '1902.30.00'
ncm_suco = '2009.8913'
ncm_agua = '2202.10.00'

#NOTE - API's
def produtos_anota_ai():
    """
    Função responsável por listar produtos do sistema Anota Ai.
    Return:
        - Json
    """
    url = "https://api-menu.anota.ai/partnerauth/v2/nm-category/rest/simple-item/export"

    headers = {
        "Authorization": Authorization,
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        pass


def incluir_produto(dic_produtos):
    """
    Função responsável pelo cadastro de produtos no sistema Omie.
    Parâmetros:
        - Dicionário contendo dados dos produtos.
    Returns:
        - response.json()
    """
    payload = json.dumps({
    'call': 'IncluirProduto',
    'app_key': app_key,
    'app_secret': app_secret,
    'param': [
        {   
            "codigo": dic_produtos["codigo_produto"],
            "descricao": dic_produtos["nome_produto"],
            "ncm": dic_produtos["ncp"],
            "valor_unitario": dic_produtos["valor_produto"],
            "unidade": "UND",
            "codigo_produto_integracao": dic_produtos["codigo_integracao"],
            "codigo_familia": dic_produtos["codigo_familia"]
        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }


    response = request(method='POST', url=endpoint_incluir_produtos, headers=headers, data=payload)
    print(response.json())
    if response.status_code == 200:
        print('Produto cadastrado com sucesso')
        return response.json()
    else:
        print('Não Foi possivel cadastrar produto')
        pass


def listar_familia_produto():
    """
    Função responsável por listar familia de produtos do sistema Omie.
    return:
        - json
    """
    payload = json.dumps({
    'call': 'PesquisarFamilias',
    'app_key': app_key,
    'app_secret': app_secret,
    'param': [
        {   
            "pagina": 1,
            "registros_por_pagina": 500
            
        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }


    response = request(method='POST', url=endpoint_listar_familias, headers=headers, data=payload)
   
    if response.status_code == 200:
        return response.json()
    else:
        pass


#SECTION - Funções

def verificar_produto(nome_produto):
    """
    Essa função é responsável por verificar se o produto pertence a lista de itens 
    que estão no cardápio.

    Parâmetros:
        - nome do produdo 
    Return: dicionário
        - ncm do produto
        - codigo do produto
    """
    dados_produtos = {}
    if nome_produto == "Refrigerante 1 litro":
        codigo_produto = gerar_codigo()
        ncm = '2202.10.00'
        dados_produtos["ncm"] = ncm
        dados_produtos["codigo_produto"] = codigo_produto
        return dados_produtos
    if nome_produto == "Refrigerante em lata":
        codigo_produto = gerar_codigo()
        ncm = '2202.10.00'
        dados_produtos["ncm"] = ncm
        dados_produtos["codigo_produto"] = codigo_produto
        return dados_produtos
    if nome_produto == "Cerveja":
        codigo_produto = gerar_codigo()
        ncm = '2203.00.00'
        dados_produtos["ncm"] = ncm
        dados_produtos["codigo_produto"] = codigo_produto
        return dados_produtos
    if nome_produto == "Agua Mineral":
        codigo_produto = gerar_codigo()
        ncm = '0210.12.00'
        dados_produtos["ncm"] = ncm
        dados_produtos["codigo_produto"] = codigo_produto
        return dados_produtos
    if nome_produto == "Agua Mineral com Gás":
        codigo_produto = gerar_codigo()
        ncm = '2201.10.00'
        dados_produtos["ncm"] = ncm
        dados_produtos["codigo_produto"] = codigo_produto
        return dados_produtos
    if nome_produto == "Refrigerante Limoneto H2oh 500ml":
        codigo_produto = gerar_codigo()
        ncm = '2202.10.00'
        dados_produtos["ncm"] = ncm
        dados_produtos["codigo_produto"] = codigo_produto
        return dados_produtos
    if nome_produto == "Água Tônica Diet Antarctica 350ml":
        codigo_produto = gerar_codigo()
        ncm = '2202.10.00'
        dados_produtos["ncm"] = ncm
        dados_produtos["codigo_produto"] = codigo_produto
        return dados_produtos
    if nome_produto == "Refrigerante Limão H2oh Limão 500ml":
        codigo_produto = gerar_codigo()
        ncm = '2202.10.00'
        dados_produtos["ncm"] = ncm
        dados_produtos["codigo_produto"] = codigo_produto
        return dados_produtos


def familia_produtos():
    """
    Essa função 'chama' a API da omie de listar familia de produtos e cria um dicionário,
    onde a chave é o nome da familia e o valor o código da familia.

    Return: dicionário
        - nome da familia
        - código do produto
    """
    dados  = listar_familia_produto()
    familia_produtos = dados["famCadastro"]
    dicionario_familia_produtos = {}

    for familia in familia_produtos:
        nome = familia["nomeFamilia"]
        codigo = familia["codigo"]
        dicionario_familia_produtos[nome] = codigo
    
    return dicionario_familia_produtos


# Lista para armazenar códigos gerados
codigos_gerados = set()

def gerar_codigo():
    """
    Essa função Gera um código aletatório, que será utilizado para cadastro
    do código do produdo vindo o sistema Anota Ai
    """
    while True:
        numero = random.randint(100000, 999999)
        codigo = f'p{numero}'

        # Verifique se o código já foi gerado, se não, retorne-o
        if codigo not in codigos_gerados:
            codigos_gerados.add(codigo)
            return codigo



def verificar_familia(nome_familia, nome_produto):
    """
    Essa função recebe o nome da familia do produto do Anota Ai e verifica se o mesmo se seu nome.
    Após fazer a identificação, adiciona na variável 'nome' a nomeclatura correta da família do produto.

    Parâmetros:
        - Nome da familia
        - Nome do produto
    Return
        - nome da familia do produto
    """
    dic_dados = {}
    if nome_familia == 'Adicionais':
        nome = 'Insumos'        
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_insumos
        return dic_dados
    if nome_familia == 'Bebida' and nome_produto.startswith('Suco'):
        nome = 'SUCOS'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_suco
        return dic_dados
    if nome_familia == 'Bebidas' and nome_produto.startswith('Suco'):
        nome = 'SUCOS'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_suco
        return dic_dados
    if nome_familia == 'Bebidas' and nome_produto.startswith('Agua'):
        nome = 'ÁGUA'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_agua
        return dic_dados
    if nome_familia == 'Bebidas' and nome_produto.startswith('Agua'):
        nome = 'ÁGUA'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_agua
        return dic_dados
    if nome_familia == 'Bebidas' and nome_produto.startswith('Água'):
        nome = 'ÁGUA'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_agua
        return dic_dados
    if nome_familia == 'Bebidas' and nome_produto == 'Cerveja':
        nome = 'Cerveja'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_cerveja
        return dic_dados
    if nome_familia == 'Bebidas':
        nome = 'Refrigerantes'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_refrigerantes
        return dic_dados
    if nome_familia == 'Bebida':
        nome = 'Refrigerantes'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_refrigerantes
        return dic_dados
    if nome_familia == 'Borda PEQUENA (4 PEDAÇOS)':
        nome = 'Insumos'              
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_insumos
        return dic_dados
    if nome_familia == 'Deseja adicionar Bebidas':
        nome = 'Refrigerantes'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_refrigerantes
        return dic_dados
    if nome_familia == 'Escolha a sua Preferência':
        nome = 'Insumos'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_insumos
        return dic_dados
    if nome_familia == 'Molhos':
        nome = 'Insumos'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_insumos
        return dic_dados
    if nome_familia == 'Pizza Doce P':
        nome = 'Pizzas'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_pizza
        return dic_dados
    if nome_familia ==  'sabor GRANDE (8 PEDAÇOS)':
        nome = 'Pizzas'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_pizza
        return dic_dados
    if nome_familia == 'Sabor PEQUENA (4 PEDAÇOS)':
        nome = 'Pizzas'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_pizza
        return dic_dados
    if nome_familia == 'Sabores':
        nome = 'Refrigerantes'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_refrigerantes
        return dic_dados
    if nome_familia == 'Turbine seu Warp':
        nome = 'Insumos'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_insumos
        return dic_dados
    if nome_familia == 'Turbine sua Batata Frita':
        nome = 'Insumos'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_insumos
        return dic_dados
    if nome_familia == 'Porção':
        nome = 'Porção'
        dic_dados["nome"] = nome
        dic_dados["ncm"] = ncm_porcoes
        return dic_dados
#NOTE - Chamada de funções
dicionario_familia_produtos = familia_produtos()

#SECTION - Main code

produtos_pizzaria = produtos_anota_ai()
produtos = produtos_pizzaria["categories"]
lista_produtos = []


for itens_produtos in produtos:
    categoria = itens_produtos["title"]
    itens = itens_produtos["itens"]
    nome_familia = itens_produtos["title"]
    
    
    for prod in itens:
        dic_produtos = {}
        nome_produto = prod["title"]
        valor_produto = prod["price"] 

        dic_dados = verificar_familia(nome_familia, nome_produto)
        if dic_dados != None:
            familia = dic_dados["nome"]
            ncm = dic_dados["ncm"]
        
        if familia == None:
            codigo_familia = dicionario_familia_produtos.get(nome_familia, None)
        else:
            codigo_familia = dicionario_familia_produtos.get(familia, None)

        if categoria == 'Bebida':
            ncm = '0210.12.00'
            codigo_produto = 123456
        elif categoria == 'Cerveja':
            ncm = '2203.00.00'
            codigo_produto = 654321
               
           
        dados_produto = verificar_produto(nome_produto) 
        if dados_produto == None:
            codigo_produto = gerar_codigo()
        else:    
            codigo_produto = dados_produto["codigo_produto"]
            ncm = dados_produto["ncm"]        
        
        dic_produtos["codigo_familia"] = codigo_familia
        
        random_codigo_integracao = gerar_codigo()
        dic_produtos["codigo_integracao"] = random_codigo_integracao
        dic_produtos["nome_produto"] = nome_produto
        dic_produtos["valor_produto"] = valor_produto
        dic_produtos["ncp"] = ncm
        dic_produtos["codigo_produto"] = codigo_produto
        
        lista_produtos.append(dic_produtos)
       

for lista in lista_produtos:
    incluir_produto(lista)