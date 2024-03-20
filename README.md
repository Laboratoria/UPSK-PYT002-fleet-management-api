# Software de Gestão de Frota API

## Índice

* [1. Preambulo](#1-preâmbulo)
* [2. Resumo do projeto](#2-resumo-do-projeto)
* [3. Objetivos de aprendizado](#3-objetivos-de-aprendizado)
* [4. Considerações de carácter geral](#4-considerações-de-carácter-geral)
* [5. Critérios de aceitação do projeto](#5-critérios-de-aceitação-do-projeto)
* [6. Tecnologias Utilizadas](#6-tecnologias-utilizadas)
* [7. Dicas, sugestões e leituras complementares](#7-dicas-sugestões-e-leituras-complementares)
* [8. Funcionalidades opcionais](#8-funcionalidades-opcionais)

***

## 1. Preâmbulo

De acordo com [Wikipedia](https://es.wikipedia.org/wiki/Internet_de_las_cosas),
a Internet das Coisas (IoT) é um conceito que se refere à interconexão
digital de objetos cotidianos com a internet. Constitui uma mudança
radical na qualidade de vida das pessoas na sociedade, oferecendo novas
oportunidades no acesso a dados, educação, segurança, assistência médica
e transporte, entre outros campos. Por exemplo, na logística e gestão de
frotas, é possível rastrear a localização e as condições dos veículos a
qualquer momento, por meio de sensores sem fio conectados à internet que
enviam alertas em caso de eventualidades (atrasos, danos, roubos, etc.).

![zach-vessels-utMdPdGDc8M-unsplash](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/fleet-management-api-java%2Fthumb.jpg?alt=media)

A IoT também apresenta desafios como armazenamento, análise e visualização
da grande quantidade de informações geradas. Estima-se que até 2025, os
dispositivos IoT gerem
[79.4 zettabytes](https://www.statista.com/statistics/1017863/worldwide-iot-connected-devices-data-size/)
(1 zettabyte é equivalente a 1 trilhão de gigabytes). Como desenvolvedoras,
devemos estar cientes desses desafios e contribuir para sua solução com nossa
experiência, conhecimento e vontade de aprender.

## 2. Resumo do projeto

Neste projeto, você construirá a API REST de um
[Software de Gestão de Frota](https://en.wikipedia.org/wiki/Fleet_management)
para consultar as localizações dos veículos de uma empresa de táxis
em Pequim, China.

Forneceremos as localizações de quase 10 mil táxis. Esperamos que, como
desenvolvedora, você explore novas alternativas e técnicas para armazenar
e consultar essas informações, garantindo a melhor experiência do usuário
em sua API REST.

## 3. Objetivos de aprendizagem

Reflita e depois enumere os objetivos que quer alcançar e aplique no seu projeto. Pense nisso para decidir sua estratégia de trabalho.

### Java

- [ ] **Modificadores de acesso (public, private, protected)**

- [ ] **Variáveis**

- [ ] **Uso de condicionais**

- [ ] **Uso de loops (Laços)**

#### Tipos de dados

- [ ] **Primitivos**

- [ ] **Dados primitivos vs não primitivos**

- [ ] **Cadeias de caracteres**

- [ ] **Arrays**

#### Coleções

- [ ] **ArrayList**

- [ ] **HashMap**

- [ ] **HashSet**

#### Testes

- [ ] **JUnit**

- [ ] **Mockito**

#### Spring Framework

- [ ] **Initializr**

  <details><summary>Links</summary><p>

  * [Spring Initializr](https://start.spring.io/)
</p></details>

- [ ] **Spring Boot**

  <details><summary>Links</summary><p>

  * [Spring Boot Reference Documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/)
</p></details>

- [ ] **Controladores**

- [ ] **Serviços**

- [ ] **Spring Data JPA**

  <details><summary>Links</summary><p>

  * [Spring Data JPA - Reference Documentation](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/)
</p></details>

- [ ] **Entidade**

- [ ] **Repositório**

##### Conceitos Principais _(Spring Framework)_

- [ ] **Beans**

- [ ] **Inversão de Controle**

- [ ] **Anotações**

##### Spring Web _(Spring Framework)_

- [ ] **RestController**

- [ ] **RequestMapping**

- [ ] **RequestParam**

##### Testes _(Spring Framework)_

- [ ] **Spring Test**

- [ ] **Hamcrest**

#### Hibernate ORM

- [ ] **Configuração**

- [ ] **Esquema**

- [ ] **Entidade**

- [ ] **Tabela**

- [ ] **Coluna**

- [ ] **Identificadores**

- [ ] **Associações**

- [ ] **Coleções**

- [ ] **Persistência**

- [ ] **Consultas**

### Python

- [ ] **Variáveis (declaração, atribuição, escopo)**

  <details><summary>Links</summary><p>

  * [Variables in Python – Real Python (em inglês)](https://realpython.com/python-variables/)
  * [Variables in Python - GeeksforGeeks (em inglês)](https://www.geeksforgeeks.org/python-variables/)
</p></details>

- [ ] **Uso de condicionais (if, elif, ternário)**

  <details><summary>Links</summary><p>

  * [Conditional Statements in Python – Real Python (em inglês)](https://realpython.com/python-conditional-statements/)
</p></details>

- [ ] **Operadores (identidade, aritméticos, comparação etc)**

  <details><summary>Links</summary><p>

  * [Python Operators - GeeksforGeeks (em inglês)](https://www.geeksforgeeks.org/python-operators/)
</p></details>

- [ ] **Docstrings (e sua diferença de comentários)**

  <details><summary>Links</summary><p>

  * [Docstrings - Python Docs (em inglês)](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)
</p></details>

- [ ] **Linting (pylint)**

  <details><summary>Links</summary><p>

  * [Pylint - Documentação oficial](https://pylint.pycqa.org/en/latest/)
  * [Linting Python in Visual Studio Code - Visual Studio Code Docs (em inglês)](https://code.visualstudio.com/docs/python/linting)
</p></details>

- [ ] **Serialização (e deserialização)**

  <details><summary>Links</summary><p>

  * [Serialize Your Data With Python – Real Python (em inglês)](https://realpython.com/python-serialize-data/)
</p></details>

#### Tipos de dados

- [ ] **Tipos de dados primitivos (int, float, str, bool)**

  <details><summary>Links</summary><p>

  * [Data Types - Python Docs (em inglês)](https://docs.python.org/3/library/datatypes.html)
  * [Data types in Python (em inglês)](https://www.educative.io/answers/data-types-in-python)
</p></details>

- [ ] **Listas (arrays)**

  <details><summary>Links</summary><p>

  * [Lists - Python Docs (em inglês)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
  * [Lists and Tuples in Python - Real Python (em inglês)](https://realpython.com/python-lists-tuples/)
</p></details>

- [ ] **Tuples**

  <details><summary>Links</summary><p>

  * [Tuples - Python Docs (em inglês)](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
  * [Lists and Tuples in Python - Real Python (em inglês)](https://realpython.com/python-lists-tuples/)
</p></details>

- [ ] **Dictionaries (Dicts)**

  <details><summary>Links</summary><p>

  * [Dictionaries - Python Docs (em inglês)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
  * [Dictionaries in Python - Real Python (em inglês)](https://realpython.com/python-dicts/)
</p></details>

- [ ] **Sets**

  <details><summary>Links</summary><p>

  * [Sets - Python Docs (em inglês)](https://docs.python.org/3/tutorial/datastructures.html#sets)
  * [Sets in Python - Real Python (em inglês)](https://realpython.com/python-sets/)
</p></details>

#### Funções

- [ ] **Conceitos básicos (parâmetros, argumentos, valores padrão, retorno)**

  <details><summary>Links</summary><p>

  * [Defining Functions - Python Docs (em inglês)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
  * [Python Functions - GeeksforGeeks (em inglês)](https://www.geeksforgeeks.org/python-functions/)
</p></details>

- [ ] ***args e **kwargs**

  <details><summary>Links</summary><p>

  * [*args and **kwargs in Python - GeeksforGeeks (em inglês)](https://www.geeksforgeeks.org/args-kwargs-python/)
</p></details>

- [ ] **Encerramentos (closures)**

  <details><summary>Links</summary><p>

  * [Closures - Python Docs (em inglês)](https://docs.python.org/3/reference/datamodel.html#emulating-closures-and-nested-scope)
</p></details>

- [ ] **Funções lambda**

  <details><summary>Links</summary><p>

  * [Lambda Functions - Python Docs (em inglês)](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
  * [How to Use Python Lambda Functions – Real Python (em inglês)](https://realpython.com/python-lambda/)
</p></details>

- [ ] **Decoradores**

  <details><summary>Links</summary><p>

  * [Decorators - Python Docs (em inglês)](https://docs.python.org/3/glossary.html#term-decorator)
  * [Decorators in Python - Geeks for Geeks (em inglês)](https://www.geeksforgeeks.org/decorators-in-python/)
</p></details>

#### Iteração

- [ ] **Uso de loops (while, for..in)**

  <details><summary>Links</summary><p>

  * [Loops in Python - For, While and Nested Loops - GeeksforGeeks](https://www.geeksforgeeks.org/loops-in-python/)
  * [Loops - Learn Python - Free Interactive Python Tutorial](https://www.learnpython.org/en/Loops)
</p></details>

- [ ] **Compreensão de listas**

  <details><summary>Links</summary><p>

  * [List Comprehension - Python Docs (em inglês)](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
  * [List Comprehension in Python - GeeksforGeeks (em inglês)](https://www.geeksforgeeks.org/list-comprehensions-in-python/)
  * [When to Use a List Comprehension in Python – Real Python](https://realpython.com/list-comprehension-python/)
</p></details>

- [ ] **Técnicas funcionais (map, filter, reduce)**

  <details><summary>Links</summary><p>

  * [Our Guide to Map, Filter, and Reduce Functions in Python - Udacity (em inglês)](https://www.udacity.com/blog/2020/12/our-guide-to-map-filter-and-reduce-functions-in-python.html)
  * [Map, Filter, Reduce - Learn Python - Free Interactive Python Tutorial (em inglês)](https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce)
</p></details>

#### Testes em Python

- [ ] **Testes unitários (unit tests, unittest, pytest)**

  <details><summary>Links</summary><p>

  * [unittest - Python Docs (em inglês)](https://docs.python.org/3/library/unittest.html)
  * [pytest - Documentação oficial](https://docs.pytest.org/en/6.2.x/)
</p></details>

- [ ] **Uso de mocks (e patch)**

  <details><summary>Links</summary><p>

  * [unittest.mock - Python Docs (em inglês)](https://docs.python.org/3/library/unittest.mock.html)
  * [unittest.mock - Python Docs (em inglês)](https://docs.python.org/3/library/unittest.mock.html)
</p></details>

- [ ] **Uso de fixtures**

  <details><summary>Links</summary><p>

  * [Fixtures do pytest - Documentação oficial](https://docs.pytest.org/en/6.2.x/fixture.html)
</p></details>

#### Modularização

- [ ] **Módulos**

  <details><summary>Links</summary><p>

  * [Módulos - Python Docs (em inglês)](https://docs.python.org/3/tutorial/modules.html)
</p></details>

- [ ] **Pacotes**

  <details><summary>Links</summary><p>

  * [Pacotes - Python Docs (em inglês)](https://docs.python.org/3/tutorial/modules.html#packages)
</p></details>

#### Gerenciamento de dependências

- [ ] **pip (instalação e uso de pacotes)**

  <details><summary>Links</summary><p>

  * [pip - Python Docs (em inglês)](https://docs.python.org/3/installing/index.html)
</p></details>

- [ ] **Ambiente Virtual (ambientes virtuais, virtualenv)**

  <details><summary>Links</summary><p>

  * [venv — Creation of virtual environments — Python 3.12.2 documentation (em inglês)](https://docs.python.org/3/library/venv.html)
  * [Python Virtual Environments: A Primer – Real Python (em inglês)](https://realpython.com/python-virtual-environments-a-primer/)
</p></details>

- [ ] **requirements.txt**

  <details><summary>Links</summary><p>

  * [requirements.txt - Documentação oficial](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
</p></details>

#### Flask

##### Rotas _(Flask)_

- [ ] **Decorador de rota**

  <details><summary>Links</summary><p>

  * [Routing - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing)
</p></details>

- [ ] **Função de visualização**

  <details><summary>Links</summary><p>

  * [Funções de visualização - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#view-functions)
</p></details>

- [ ] **Regras de variáveis (urls dinâmicas)**

  <details><summary>Links</summary><p>

  * [Regras de Variáveis - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules)
</p></details>

##### Objeto de Requisição _(Flask)_

- [ ] **Argumentos**

  <details><summary>Links</summary><p>

  * [Requisição - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data)
</p></details>

- [ ] **Cabeçalhos**

  <details><summary>Links</summary><p>

  * [Requisição - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data)
</p></details>

##### Objeto de Resposta _(Flask)_

- [ ] **Partes da resposta (status, corpo, cabeçalhos)**

  <details><summary>Links</summary><p>

  * [Resposta - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#about-responses)
</p></details>

- [ ] **jsonify**

  <details><summary>Links</summary><p>

  * [jsonify - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify)
</p></details>

##### Testando no Flask _(Flask)_

- [ ] **Configuração de fixtures**

  <details><summary>Links</summary><p>

  * [Testando - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/testing/#fixtures)
</p></details>

- [ ] **Cliente de teste**

  <details><summary>Links</summary><p>

  * [Testando - Flask Docs (em inglês)](https://flask.palletsprojects.com/en/3.0.x/testing/#sending-requests-with-the-test-client)
</p></details>

#### Django

- [ ] **Visualizações**

  <details><summary>Links</summary><p>

  * [Visualizações base](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/)
</p></details>

- [ ] **Testando**

  <details><summary>Links</summary><p>

  * [Testando no Django](https://docs.djangoproject.com/en/5.0/topics/testing/)
  * [Testando o framework rest](https://www.django-rest-framework.org/api-guide/testing/#testing)
</p></details>

- [ ] **queryset**

  <details><summary>Links</summary><p>

  * [O argumento queryset](https://www.django-rest-framework.org/api-guide/relations/#the-queryset-argument)
</p></details>

- [ ] **Filtro**

  <details><summary>Links</summary><p>

  * [Filtragem](https://www.django-rest-framework.org/api-guide/filtering/)
</p></details>

- [ ] **Ordenar Por**

  <details><summary>Links</summary><p>

  * [OrderingFilter](https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter)
</p></details>

- [ ] **URLs (Path, URLconf, urlpatterns)**

  <details><summary>Links</summary><p>

  * [URLs do Django](https://tutorial.djangogirls.org/en/django_urls/)
  * [Despachador de URL](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
</p></details>

##### Configuração _(Django)_

- [ ] **Migrações**

  <details><summary>Links</summary><p>

  * [Migrações](https://docs.djangoproject.com/es/5.0/topics/migrations/#module-django.db.migrations)
</p></details>

- [ ] **Configuração do aplicativo**

  <details><summary>Links</summary><p>

  * [Aplicativos instalados](https://docs.djangoproject.com/es/5.0/ref/settings/#std-setting-INSTALLED_APPS)
</p></details>

##### Modelos _(Django)_

- [ ] **Campos**

  <details><summary>Links</summary><p>

  * [Tipos de campos](https://docs.djangoproject.com/en/5.0/topics/db/models/#Fields)
</p></details>

- [ ] **Chave Estrangeira**

  <details><summary>Links</summary><p>

  * [Referência do campo do modelo](https://docs.djangoproject.com/en/5.0/ref/models/fields/)
</p></details>

##### Rest Framework _(Django)_

- [ ] **Serializadores**

  <details><summary>Links</summary><p>

  * [Serializadores](https://www.django-rest-framework.org/community/third-party-packages/#serializers)
</p></details>

- [ ] **Paginação**

  <details><summary>Links</summary><p>

  * [Paginação](https://www.django-rest-framework.org/api-guide/pagination/#pagination)
</p></details>

- [ ] **Parâmetros da consulta**

  <details><summary>Links</summary><p>

  * [query_params](https://www.django-rest-framework.org/api-guide/requests/#query_params)
</p></details>

- [ ] **ViewSet**

  <details><summary>Links</summary><p>

  * [ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#viewset)
</p></details>

- [ ] **Apiview**

  <details><summary>Links</summary><p>

  * [GenericAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)
</p></details>

### Programação Orientada a Objetos (POO)

- [ ] **Classes**

- [ ] **Objetos**

- [ ] **Métodos**

- [ ] **Atributos**

- [ ] **Construtores**

- [ ] **Encapsulamento**

- [ ] **Abstração**

- [ ] **Composição**

- [ ] **Interfaces**

- [ ] **Herança (super, extends, override)**

- [ ] **Linguagem de Modelagem Unificada (UML, diagramas de classe)**

### Node.js

- [ ] **Instalar e usar módulos com npm**

  <details><summary>Links</summary><p>

  * [Sitio oficial de npm (em inglês)](https://www.npmjs.com/)
</p></details>

- [ ] **Configuração do package.json**

  <details><summary>Links</summary><p>

  * [package.json - Documentação oficial (em inglês)](https://docs.npmjs.com/files/package.json)
</p></details>

- [ ] **Configuração do npm-scripts**

  <details><summary>Links</summary><p>

  * [scripts - Documentação oficial (em inglês)](https://docs.npmjs.com/misc/scripts)
</p></details>

- [ ] **process (env, argv, stdin-stdout-stderr, exit-code)**

  <details><summary>Links</summary><p>

  * [Process - Documentação oficial (em inglês)](https://nodejs.org/api/process.html)
</p></details>

- [ ] **File system (fs, path)**

  <details><summary>Links</summary><p>

  * [File system - Documentação oficial (em inglês)](https://nodejs.org/api/fs.html)
  * [Path - Documentação oficial (em inglês)](https://nodejs.org/api/path.html)
</p></details>

### SQL

- [ ] **Criação e modificação de tabelas**

  <details><summary>Links</summary><p>

  * [SQL CREATE TABLE Statement - w3schools (em inglês)](https://www.w3schools.com/sql/sql_create_table.asp)
  * [CREATE TABLE Statement - PostgreSQL Docs (em inglês)](https://www.postgresql.org/docs/9.1/sql-createtable.html)
  * [ALTER TABLE Statement - PostgreSQL Docs (em inglês)](https://www.postgresql.org/docs/9.1/sql-altertable.html)
</p></details>

- [ ] **Operações CRUD (Create-Read-Update-Delete)**

  <details><summary>Links</summary><p>

  * [INSERT](https://www.postgresql.org/docs/9.5/sql-insert.html)
  * [SELECT](https://www.postgresql.org/docs/9.5/sql-select.html)
  * [UPDATE](https://www.postgresql.org/docs/9.1/sql-update.html)
  * [DELETE](https://www.postgresql.org/docs/8.1/sql-delete.html)
</p></details>

- [ ] **Exclusão de tabelas ou bancos de dados inteiros com DROP**

  <details><summary>Links</summary><p>

  * [DROP TABLE](https://www.postgresql.org/docs/8.2/sql-droptable.html)
  * [DROP DATABASE](https://www.postgresql.org/docs/8.2/sql-dropdatabase.html)
</p></details>

### Bases de dados

- [ ] **Modelagem de dados**

- [ ] **Conexão**

- [ ] **Índices e limitações**

### PostgreSQL

- [ ] **Tipos de dados**

  <details><summary>Links</summary><p>

  * [Chapter 8. Data Types - Docs (em inglês)](https://www.postgresql.org/docs/14/datatype.html)
</p></details>

- [ ] **Índices**

  <details><summary>Links</summary><p>

  * [Chapter 11. Indexes - Docs (em inglês)](https://www.postgresql.org/docs/14/indexes.html)
</p></details>

## 4. Considerações de carácter geral

* Este projeto deve ser "resolvido" em pares.
* O intervalo de tempo estimado para concluir o projeto é de 4 a 6 Sprints.

## 5. Critérios de aceitação do projeto

Nossa cliente instalou dispositivos GPS em seus táxis. Esses dispositivos
usam sinais de satélite para determinar com precisão as coordenadas
geográficas do táxi.

Nossa cliente requer:

1. Carregar as informações dos arquivos SQL para um banco de dados
PostgreSQL.
2. Desenvolver uma API REST que permita consultar, por meio de requisições
HTTP, as informações armazenadas no banco de dados.

### Definição do produto

O [_Product Owner_](https://www.youtube.com/watch?v=r2hU7MVIzxs&t=202s)
nos apresenta este _backlog_ que é o resultado de seu trabalho com a
cliente até hoje.

***

#### [História do usuário 1] Carregar informações no banco de dados

Eu, como desenvolvedora, quero carregar as informações armazenadas até
agora em
[arquivos SQL](https://drive.google.com/file/d/1T5m6Vzl9hbD75E9fGnjbOiG2UYINSmLx/view?usp=drive_link)
em um banco de dados PostgreSQL, para facilitar sua consulta e análise.

##### Critérios de aceitação

* Deve-se considerar o seguinte diagrama para a implementação das
relações entre as tabelas

![mer](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/fleet-management-api-java%2Fsql-diagram.png?alt=media)

* A tabela de _trajectories_ deve ser criada com o "id" que aumenta
automaticamente (SERIAL) para poder inserir os valores sem a necessidade de
especificar um identificador.

##### Definição de pronto

* O banco de dados tem a tabela de táxis criada.
* A tabela de táxis tem os dados dos táxis carregados.
* O banco de dados tem a tabela de trajetórias criada.
* A tabela de trajetórias tem os dados das trajetórias dos táxis carregados.

***

##### [História do usuário 2] Endpoint de listagem de táxis

Eu, como cliente da API REST, necessito de um _endpoint_ para listar
todos os táxis.

##### Critérios de aceitação

* O _endpoint_ responde para cada táxi: id e placa.
* O _endpoint_ paginamos os resultados para garantir que as respostas
sejam mais fáceis de manejar.

##### Definição de pronto

* Há documentação no [Swagger](https://swagger.io/) para o _endpoint_
desenvolvido, especificando
[método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods),
url, parâmetros,
[cabeçalhos](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
[códigos HTTP de resposta](https://shorturl.at/bdegB) e corpo.
* O código do _endpoint_ deve passar por revisão de código de pelo menos uma colega.
* O código do _endpoint_ deve ser carregado em um repositório do Github.
* O código do _endpoint_ deve ter testes unitários e de ponta a ponta.

***

#### [História do usuário 3] Endpoint de histórico de localizações

Eu, como cliente da API REST, necessito de um _endpoint_ para consultar
todas as localizações de um táxi dado o id do táxi e uma data.

##### Critérios de aceitação

* O _endpoint_ responde para o id do táxi e uma data consultado as
  seguintes informações: latitude, longitude e timestamp (data e hora).
* O _endpoint_ paginamos os resultados para garantir que as respostas sejam
mais fáceis de manejar.

##### Definição de pronto

* Há documentação no [Swagger](https://swagger.io/) para o _endpoint_
desenvolvido, especificando
[método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods),
url, parâmetros,
[cabeçalhos](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
[códigos HTTP de resposta](https://shorturl.at/bdegB) e corpo.
* O código do _endpoint_ deve passar por revisão de código de pelo menos uma colega.
* O código do _endpoint_ deve ser carregado em um repositório do Github.
* O código do _endpoint_ deve ter testes unitários e de ponta a ponta.

***

#### [História do usuário 4] Endpoint de última localização

Eu, como cliente da API REST, necessito de um _endpoint_ para consultar a
última localização reportada por cada táxi.

##### Critérios de aceitação

* O _endpoint_ responde para cada táxi as seguintes informações: id, placa,
latitude, longitude e timestamp (data e hora).
* O _endpoint_ paginamos os resultados para garantir que as respostas sejam
mais fáceis de manejar.

##### Definição de pronto

* Há documentação no [Swagger](https://swagger.io/) para o _endpoint_
desenvolvido, especificando
[método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods),
url, parâmetros,
[cabeçalhos](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
[códigos HTTP de resposta](https://shorturl.at/bdegB) e corpo.
* O código do _endpoint_ deve passar por revisão de código de pelo menos uma colega.
* O código do _endpoint_ deve ser carregado em um repositório do Github.
* O código do _endpoint_ deve ter testes unitários e de ponta a ponta.

***

## 6. Tecnologias Utilizadas

Você pode implementar este projeto em JavaScript, Python, ou Java.

* [NodeJs](./docs/stack-node.md)
* [Python](./docs/stack-python.md)
* [Java](./docs/stack-java.md)

## 7. Dicas, sugestões e leituras complementares

### Modelagem de dados

O banco de dados recomendado para sua aplicação é o PostgreSQL. Recomendamos
o uso do [vercel Postgresql](https://vercel.com/docs/storage/vercel-postgres)
para que você não precise instalar o PostgreSQL em seu computador.

Uma vez que você tenha acesso a uma instância do PostgreSQL, deverá criar
tabelas em seu banco de dados para armazenar as informações fornecidas.
Recomendamos criar duas tabelas, uma para armazenar as informações dos táxis
e outra para armazenar as informações de localização. Você deverá definir as
colunas de cada tabela de acordo com as informações fornecidas.

Você pode criar uma tabela no PostgreSQL usando
[SQL](https://www.postgresqltutorial.com/postgresql-create-table/).

### Definir endpoints da API

Você deverá definir e documentar os endpoints de sua API. Deve usar
[Swagger](https://swagger.io/) para isso.

Para uma API REST, é necessário definir, para cada endpoint, entre outras coisas,
o [método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), url,
parâmetros, [cabeçalhos](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
[códigos HTTP de resposta](https://shorturl.at/bdegB) e corpo.

Por exemplo, na figura a seguir, é definido um endpoint para consultar as
informações dos táxis no aplicativo. O método do endpoint é _GET_, a url
é _/taxis_. Ele recebe um parâmetro de _query_, retorna as informações com
o _código HTTP_ 200 em formato json, graças ao _header_ `Content-type` com
valor `application/json`.

![Exemplo de Endpoint API Rest](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/fleet-management-api-java%2Fexample-endpoint-api-rest.png?alt=media)

## 8. Funcionalidades Opcionais

Se você completou todas as funcionalidades do projeto, convidamos você a
trabalhar nas [funcionalidades opcionais](./docs/extension.md)
