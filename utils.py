# utils.py
# Funções utilitárias para o projeto

import smtplib
from email.mime.text import MIMEText
import requests
import pandas as pd
from fpdf import FPDF
import os
import json

def ler_ceps_csv(nome_arquivo):
    """Lê um arquivo CSV com a lista de CEPs e retorna uma lista."""
    try:
        df = pd.read_csv(nome_arquivo)
        return df["CEP"].tolist()  # Assumindo que a coluna com os CEPs se chama "CEP"
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return []

def consultar_cep_2(cep, url_base):
    try:
        url = url_base.format(cep)
        response = requests.get(url)
        dados = json.loads(response.text)
        if dados.get("numero") == "":
            dados["numero"] = "Não informado"
        return {"CEP": cep, 
                "Estado": dados.get("estado", ""), 
                "Cidade": dados.get("cidade" , ""), 
                "Bairro": dados.get("bairro", ""), 
                "Rua": dados.get("logradouro", ""), 
                "Número": dados.get("numero", "")}
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar CEP {cep}: {e}")
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