# FUNÇÃO 1: Formata o nome (já pronta)
def formatar_nome(nome):
    # Para cada palavra do nome, coloca a 1ª letra maiúscula
    # e junta tudo com espaço
    # Ex: "ana silva" -> ["ana", "silva"] -> ["Ana", "Silva"] -> "Ana Silva"
    return ' '.join(palavra.capitalize() for palavra in nome.strip().split())


# FUNÇÃO 2: Valida o e-mail (AQUI É O TODO)
def validar_email(email):
    # Conta quantos '@' existem no e-mail
    # Deve ter EXATAMENTE 1
    if email.count('@') != 1:
        return False

    # Divide o e-mail pelo '@'
    # Ex: "ana.silva@email.com" -> ["ana.silva", "email.com"]
    partes = email.split('@')

    # partes[1] é tudo que vem DEPOIS do '@'
    # Ex: "email.com"
    # Verifica se tem pelo menos um '.' após o '@'
    if '.' not in partes[1]:
        return False

    # Se passou pelas duas verificações, o e-mail é válido
    return True


# FUNÇÃO 3: Processa a entrada (já pronta)
def processar_cadastro(entrada):
    # Verifica se existe ", " na entrada
    # Se não tiver, a entrada está mal formatada
    if ', ' not in entrada:
        return 'Entrada inválida - ERRO'

    # Divide pelo ", " — mas só na PRIMEIRA ocorrência (maxsplit=1)
    # Ex: "ana silva, ana.silva@email.com" -> ["ana silva", "ana.silva@email.com"]
    nome, email = entrada.split(', ', 1)

    # Chama a função 1 para formatar o nome
    # Ex: "ana silva" -> "Ana Silva"
    nome_formatado = formatar_nome(nome)

    # Chama a função 2 para validar o e-mail
    if validar_email(email):
        return f"{nome_formatado} - OK"     # E-mail válido
    else:
        return f"{nome_formatado} - ERRO"   # E-mail inválido


# PROGRAMA PRINCIPAL
entrada = input()                    # Lê a linha do usuário
print(processar_cadastro(entrada))   # Processa e imprime o resultado