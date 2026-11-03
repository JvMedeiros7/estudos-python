import hashlib

# Exemplo de hash em Python usando a biblioteca hashlib

texto = "joãovitor"

cod = texto.encode('utf-8')  # Converte o texto em bytes

print("Texto original:", texto)
print("Hash:", cod)
print("Hash SHA-256:", hashlib.sha256(cod).hexdigest())