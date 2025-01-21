## Desafio 4 Introdução ao CodeDesign

# :rocket: Back-End

> TUDO ESTÁ BEM!!!!!.  <img src="https://user-images.githubusercontent.com/20192309/80777643-4202cd80-8b3c-11ea-8f32-5348bda4486b.jpg" width="10%" />

# Sobre a api

## Resumo da api

Aqui temos uma calculadora maluca.

### Regras de negócio

<a href="https://efficient-sloth-d85.notion.site/Desafio-04-5780c92c11534a13ab90463a18a4243d"> Desafio 4</a> <br/>

Seguindo exemplo dado pelo instrutor nesse módulo, adicione uma nova rota que retorne a média entre uma lista de números fornecida em uma requisição POST. 

A criação da nova rota deve ser chama de “calculator_4” e deve possuir todas as boas práticas conforme ensinado no módulo. Como por exemplo:

- Testes unitários
- Arquivos separados por responsabilidade (conforme feito pelo instrutor)
- Tratamento de erro em caso de um envio de requisição no formato errado

## Dependências

Para trabalhar com as depencias do python é interessante criar um ambiente virtual com o seguinte comando:

````sh
pip3 install virtualenv
````
Após executar o comando e o mesmo retornando sucesso, agora vamos entrar na pasta do projeto e abrir o terminal e executar o seguinte comando:

````sh
python3 -m virtualenv venv
````
Ele vai criar uma pasta <b>venv</b>, agora entre no terminal do projeto e execute o comando abaixo entrando nessa pasta:

````sh
cd venv/bin
````

Agora dentro dessa pasta execute o comando que irá iniciar o ambiente virtual no projeto:

````sh
source activate
````

Pronto ambiente virtual criado e ativado, caso queira ter certeza que o mesmo está ativo é só executar o comando:

````sh
pip freeze
````

Você vai ver que não vai trazer nada, agora para instalar as dependências do projeto vamos voltar para a pasta inicial do projeto:

````sh
cd ../..
````

E vamos instalar as depenências:

````sh
pip3 install -r requirements.txt
````

Para confirmar se as dependências foram instaladas corretamente é executar o comando <b>pip freeze</b> que irá trazer a lista. 

Para rodar o projeto e utilizar as rotas é só executar o comando:

````sh
python3 run.py
````

E para verificar se os testes estão passando é só executar o comando:


````sh
pytest -s -v
````


E para desativar esse ambiente virtual você pode fechar o terminal então tome cuidado, pois se fechar sem querer o seu projeto pode não funcionar mais. 

Para finalizar o ambiente virtual execute o comando:

````sh
deactivate
````

Feito com ♥ by Kayza :wave:
