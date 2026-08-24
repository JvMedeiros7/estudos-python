def mostrar_linha():
    print("-=" * 30)

def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3
