# Sistema de Gerenciamento de Finanças - Proj_CRUD

## Índice

- [Introdução](#introdução)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Banco de Dados](#banco-de-dados)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)

## Introdução

Este projeto é um sistema de gerenciamento de finanças desenvolvido para ajudar os indivíduos a controlar suas finanças de maneira eficiente.

## Tecnologias

- Python (Flask)
- SQLAlchemy
- PyMySQL
- HTML
- CSS
- JavaScript
- MySQL

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `bd.py`: Arquivo responsável pelo banco de dados.
- `templates/`: Contém os arquivos HTML do projeto.
    - `Ctabela.html`
    - `SobreNos.html`
    - `cgrafico.html`
    - `create.html`
    - `homepage.html`
    - `login.html`
    - `usuarios.html`
- `static/`: Contém arquivos estáticos como CSS e JS.
    - `Ctabela.css`
    - `SobreNos.css`
    - `form.css`
    - `grafico.js`
    - `homepage.css`
    - `style.css`
    - `style.js`
- `Imagens/`: Contém todas as imagens usadas no projeto.

## Funcionalidades

- **Criação de Conta**: Permite a criação de uma nova conta.
- **Gerenciamento de Contas Financeiras**: Adicione contas financeiras com valores e datas de vencimento.
- **Dashboard Financeiro**: Exibe um resumo financeiro.
  
## Banco de Dados

- **Tabela Pessoa**: Armazena CPF, nome, e-mail e senha.
- **Tabela Contas**: Armazena CPF, nome da conta, valor da conta e data de vencimento.

## Instalação

1. Clone o repositório.
    ```bash
    git clone <URL_DO_REPOSITÓRIO>
    ```
2. Crie e ative um ambiente virtual.
    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```
3. Instale as dependências.
    ```bash
    pip install Flask Flask-SQLAlchemy PyMySQL
    ```
4. Inicie o servidor Flask.
    ```bash
    python app.py
    ```

## Uso

1. Abra o navegador e acesse `http://localhost:5000/`.
2. Siga as instruções na tela para criar uma nova conta ou fazer login.

## Contribuição

Contribuições são bem-vindas. Abra uma issue para discutir melhorias ou correções.
