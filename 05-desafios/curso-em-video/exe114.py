import urllib.request

try:
    requisicao = urllib.request.Request(
        'https://www.pudim.com.br',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    urllib.request.urlopen(requisicao, timeout=5)
except Exception:
    print('O site pudim não está acessível no momento')
else:
    print('O site pudim está acessível!')
