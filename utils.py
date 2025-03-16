# utils.py
# Funções utilitárias para o projeto

import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fpdf import FPDF
import os

def ler_ceps_csv(nome_arquivo):
    """Lê um arquivo CSV com a lista de CEPs e retorna uma lista."""
    try:
        df = pd.read_csv(nome_arquivo)
        return df["CEP"].tolist()  # Assumindo que a coluna com os CEPs se chama "CEP"
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return []

def consultar_cep(cep, url_base):
    """Consulta um CEP no site e retorna os dados."""
    try:
        url = url_base + cep
        response = requests.get(url)
        response.raise_for_status()  # Lança exceção para erros HTTP
        soup = BeautifulSoup(response.content, "html.parser")
        # Adapte o código abaixo para extrair os dados do HTML do site
        estado = soup.find("span", {"id": "estado"}).text
        cidade = soup.find("span", {"id": "cidade"}).text
        bairro = soup.find("span", {"id": "bairro"}).text
        rua = soup.find("span", {"id": "logradouro"}).text
        numero = ""  # Adapte se o número estiver disponível
        return {"CEP": cep, "Estado": estado, "Cidade": cidade, "Bairro": bairro, "Rua": rua, "Número": numero}
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar CEP {cep}: {e}")
        return None
    except AttributeError:
        print(f"Erro ao extrair dados do CEP {cep}: Estrutura do site alterada.")
        return None

def enviar_email(destinatario, assunto, corpo, servidor, porta, usuario, senha):
    """Envia um e-mail."""
    try:
        mensagem = MIMEText(corpo)
        mensagem["Subject"] = assunto
        mensagem["From"] = usuario
        mensagem["To"] = destinatario
        with smtplib.SMTP(servidor, porta) as smtp:
            smtp.starttls()
            smtp.login(usuario, senha)
            smtp.sendmail(usuario, destinatario, mensagem.as_string())
        print(f"Email enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar email para {destinatario}: {e}")

def gerar_relatorio_pdf(dados, nome_arquivo):
    """Gera um relatório PDF com os dados."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Relatório de CEPs", ln=True, align='C')
    for dado in dados:
        pdf.cell(200, 10, txt=f"CEP: {dado['CEP']}, Estado: {dado['Estado']}, Cidade: {dado['Cidade']}, Bairro: {dado['Bairro']}, Rua: {dado['Rua']}, Número: {dado['Número']}", ln=True)
    pdf.output(nome_arquivo)
    print(f"Relatório PDF gerado: {nome_arquivo}")

def salvar_dados_csv(dados, nome_arquivo):
    """Salva os dados em um arquivo CSV."""
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False)
    print(f"Dados salvos em: {nome_arquivo}")