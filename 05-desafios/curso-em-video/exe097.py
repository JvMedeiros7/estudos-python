#Função escreva()

def escreva(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


input_msg = input("Digite uma mensagem: ")
escreva(input_msg)

input_msg2 = input("Digite outra mensagem: ")
escreva(input_msg2)

input_msg3 = input("Digite mais uma mensagem: ")
escreva(input_msg3)

