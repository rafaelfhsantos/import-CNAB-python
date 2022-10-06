# import-CNAB-python

## Esse pequeno projeto se refere a uma simples interface web que aceite upload de um arquivo CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

## É necessário ter o python e o banco de dados postgres instalado para poder executar o projeto.

- Crie um banco de dados para o projeto no postgres

- Clone o projeto e crie um ambiente virtual para o projeto

- Preencha o arquivo .env (crie ele na raíz do projeto se ele não estiver criado) com as informações referentes ao banco que criou. Pode usar o .env.example

## Criando e ativando ambiente virtual no Linux

- No diretório raiz do projeto execute ``` python -m venv venv ```

- Ative o ambiente virtual com o comando ``` source venv/bin/activate ```

## Criando e ativando ambiente virtual no Windows

- Acesse a pasta raíz do projeto e pressione as teclas ```Alt + F, S, A ``` (segure ALT, aperte f e solte, aperte S e solte, aperte A e solte e só então solte o ALT) Isso servirá para abrir o PowerShell em modo admnistrador. 

- No PowerShell, estando na raiz do projeto, execute ``` python -m venv venv ```

- Ative o ambiente virtual com o comando ``` .\venv\Scripts\activate ```

## Após Criar e Ativar o ambiente virtual (perceberá que na linha de comando terá (venv) indicando que está no ambiente virutal)

- Execute o comando ``` pip install -r requirements.txt ``` para instalar as dependências.

- Faça as migrações para criar a tabela do banco com o comando ``` python manage.py migrate ```

- Execute o projeto com ```python manage.py runserver ```

- Acesse em seu navegador a url ``` http://localhost:8000/home/ ```
