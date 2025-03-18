# Automação de Consulta de CEP, Email e Relatório PDF

Este projeto automatiza a consulta de CEPs em um site público, o envio de emails personalizados e a geração de um relatório PDF com os dados coletados.

## Pré-requisitos

* Python 3.x
* Bibliotecas instaladas (ver `requirements.txt`)

## Instalação

1. Clone o repositório.
2. Crie um ambiente virtual (opcional): `python -m venv venv`
3. Ative o ambiente virtual: `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure o arquivo `config.py` com suas informações de email.

## Execução

`python main.py`

## Melhorias

* Implementar tratamento de erros mais robusto.
* Adicionar suporte para outros sites de consulta de CEP.
* Melhorar o layout do relatório PDF.

## Disclaimer

* O site https://buscacep.com.br/ estava fora do ar e por isso, optei por usar o https://viacep.com.br/
* O relatorio poderia conter mais informações sobre a busca dos ceps como:
1. Número de Cepss sem informação.
2. Lista com Ceps para busca em outro site de consulta de ceps.
3. Lista de e-mails enviados com sucesso e e-mails retornados.