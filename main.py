# main.py
# Script principal para executar a automação

from utils import ler_ceps_csv, enviar_email, gerar_relatorio_pdf, salvar_dados_csv, consultar_cep_2
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, CEP_CONSULTA_URL_2

def main():
    ceps = ler_ceps_csv("ceps_lista_30.csv")
    dados_ceps = []
    for cep in ceps:
        dado = consultar_cep_2(cep, CEP_CONSULTA_URL_2)
        if dado:
            dados_ceps.append(dado)
    salvar_dados_csv(dados_ceps, "dados_ceps.csv")
    for dado in dados_ceps:
        assunto = f"Dados do CEP {dado['CEP']}"
        corpo = f"Estado: {dado['Estado']}\nCidade: {dado['Cidade']}\nBairro: {dado['Bairro']}\nRua: {dado['Rua']}\nNúmero: {dado['Número']}"
        enviar_email("destinatario@email.com", assunto, corpo, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
    gerar_relatorio_pdf(dados_ceps, "relatorio_ceps.pdf")

if __name__ == "__main__":
    main()