## Cadastr_de_produtos_omie

## Inicialização

### Introdução
O propósito deste projeto é realizar o cadastro de produtos vindos do sistema "Anota Ai" no ERP "Omie".

### Ferramentas
- python
- Omie - Sistema de gestão financeira do cliente
- Anota Ai

### Bibliotecas
- json: Biblioteca integrada do Python usado para converter dados em formato JSON em Python.
- requests: Realizar solicitações HTTP, permitindo interações com servidores web, APIs e comunicação na internet.
- random: possibilita a geração de números aleatórios e amostras aleatórias, sendo útil para simulações e seleções aleatórias em programação.

### Links Importantes
Documentação Omie - [Omie API Docs](https://developer.omie.com.br/service-list/)
Documentação Anota Ai - [Anota Ai API Docs](https://anota-ai.stoplight.io/docs/api-de-pedidos/ZG9jOjQxMzc1NTMy-introducao)

### Credenciais API:
app key e app secret para o ambiente da base da loja utilizado na autenticação com a API.

#### Endpoints
- endpoint_incluir_produtos: Utilizado para cadastrar produtos no sistema Omie
- endpoint_listar_familias: Utilizado para listar familias dos produtos do sistema Omie.
- url: Utilizado para obter os produtos do sistema Anota Ai.

### Funções
#### produtos_anota_ai
- A função obtém os produtos cadastrados no sistema Anota Ai.

#### incluir_produto
- A função reebe um dicionário contendo os dados do produtos do sitema Anota Ai, e o cadastra no ERP Omie. 

#### listar_familia_produto
- A função é responsável por chamar as familias dos protutos do ERP Omie.

#### verificar_produto
- A função verifica se o produto do sistema Anota Ai pertence ao grupo de itens que dicam no cardápio.

#### falimias_produtos
- A função é responsável por "chamar" a API "listar_familia_produto", a qual retorna as famílias dos produtos do ERP Omie. Em seguida, cria um dicionário onde a chave corresponde ao nome da família e o valor corresponde ao código da família.

#### gerar_codigo
-A função tem a responsabilidade de gerar códigos aleatórios que serão utilizados no cadastro de produtos no sistema Omie. O código segue um padrão que começa com a letra "p" seguida por seis números. Exemplo: "p123456".

### Carregamento de dados
O código começa chamando a função 'familia_produtos()' e, em seguida, adiciona os dados ao dicionário 'dicionario_familia_produtos'. Esses dados serão posteriormente utilizados para identificar a família do produto e atribuir seu código à variável 'codigo_familia'.

### Início do código
O script chama a função 'produtos_anota_ai()' e atribui seus valores ao dicionário 'produtos_pizzaria'. Em seguida, cria uma lista chamada 'lista_produtos', que será utilizada para armazenar os dicionários contendo os dados dos produtos a serem posteriormente cadastrados no Omie.

### Obtendo dados
Para obter os dados dos produtos, o código inicia um loop e cria um dicionário chamado 'dic_produtos'. Os dados dos produtos são então atribuídos ao dicionário com suas respectivas chaves. Durante a obtenção dos dados, o código também chama as funções 'verificar_produto', que tem a responsabilidade de verificar se o produto faz parte da lista do cardápio, e 'gerar_codigo', que é responsável por gerar o código do produto a ser cadastrado no Omie.

### Cadastrando produtos
O código cria um loop, e chama a função 'incluir_produto', que será responsável por cadastrar produtos no sistema Omie.
