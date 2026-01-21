import warnings
warnings.filterwarnings("ignore")
import requests

# Dicionário de riscos para o seu portfólio
riscos = {
    "X-Frame-Options": "Risco de Clickjacking (seu site pode ser 'sequestrado' dentro de outro).",
    "Content-Security-Policy": "Risco de Injeção de Scripts (XSS). Sem controle de fontes confiáveis.",
    "Strict-Transport-Security": "Risco de Downgrade para HTTP. O site não força conexão segura.",
    "X-Content-Type-Options": "Risco de Sniffing de MIME. O navegador pode tentar 'adivinhar' o tipo de arquivo."
}

url = input("Digite o site (ex: google.com): ")
if not url.startswith('http'):
    url = 'https://' + url

print(f"\n--- Analisando: {url} ---\n")

try:
    resposta = requests.get(url, timeout=10)
    headers = resposta.headers

    servidor = headers.get('Server', 'Não identificado')
    print(f"[ INFO ] Servidor: {servidor}")

    # Verificamos cada item do nosso dicionário de riscos
    for item, explicacao in riscos.items():
        if item in headers:
            print(f"[ ✅ ] {item}: Protegido")
        else:
            print(f"[ ❌ ] {item}: VULNERÁVEL")
            print(f"       👉 {explicacao}") # Aqui o script explica o erro!

except Exception as e:
    print(f"Erro ao conectar: {e}")