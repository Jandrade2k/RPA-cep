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

## Limitações

* O site de consulta de CEP pode alterar sua estrutura, exigindo ajustes no código.
* O envio de emails pode ser limitado pelo serviço SMTP utilizado.