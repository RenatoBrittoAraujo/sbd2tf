# Sistema montado

O sistema foi feito preparado para utilizar as seguintes tecnologias (formando o stack de ciência de dados desse projeto):

| tecnologia     | propósito                                                                        |
| -------------- | -------------------------------------------------------------------------------- |
| mysql          | base de dados cuja qual os dados são inseridos e onde serão puxados para análise |
| docker-compose | levanta um container de uma base de dados mysql local                            |
| python         | linguagem de programação que orquestra o sistema                                 |
| pymysql        | biblioteca de python que facilita o uso do MySQL                                 |
| sqlalchemy     | trabalha com pymysql permite utilizar com ORM em código                          |
| pandas + numpy | permite manipulações do dado, e também análise estatística                       |

## Para rodar (apenas linux)

1. Instale python3 `sudo apt install python3`
2. Instale as bibliotecas com pip `pip install -r requirements.txt`
3. Instale docker-compose `sudo apt install docker-compose`
4. Execute o container mysql na porta 8001 `sudo docker-compose up`
5. Em outro terminal, rode cada um os arquivos `.py` de interesse com `python3 3_sistema.py`

