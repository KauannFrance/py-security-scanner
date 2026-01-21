import warnings
warnings.filterwarnings("ignore")
import requests


# Pergunta qual site analisar
url = input("Digite o site (ex: google.com): ")

if not url.startswith('http'):
    url = 'https://' + url

print(f"\n--- Analisando: {url} ---\n")

try:
    # Faz a conexão com o site
    resposta = requests.get(url)
    headers = resposta.headers

    # Verifica o servidor (Banner Grabbing)
    servidor = headers.get('Server', 'Não identificado')
    print(f"[ INFO ] Servidor: {servidor}")

    # Lista de escudos de segurança
    seguranca = ["X-Frame-Options", "Content-Security-Policy", "Strict-Transport-Security"]

    for item in seguranca:
        if item in headers:
            print(f"[ ✅ ] {item}: Protegido")
        else:
            print(f"[ ❌ ] {item}: VULNERÁVEL (Faltando)")

except Exception as e:
    print(f"Erro ao conectar: {e}")