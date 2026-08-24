cadastro = []

while True:
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas cadastradas")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da pessoa: ")
        ano_nasc = input("Digite o ano de nascimento da pessoa: ")
        idade = 2026 - int(ano_nasc)
        
        num_ctps = input("Digite o número da carteira de trabalho da pessoa: ")
        ano_contratação = None
        salario = None
        if num_ctps != "0":
            ano_contratação = input("Digite o ano de contratação da pessoa: ")
            salario = input("Digite o salário da pessoa: ")


        if idade > 65: 
            print("Você está aposentado.")
        else:
            tempo_aposentadoria = 65 - idade
            print(f"Faltam {tempo_aposentadoria} anos para você se aposentar.")
            
        pessoa = {"nome": nome, "idade": idade, "num_ctps": num_ctps, "ano_contratação": ano_contratação, "salario": salario}
        cadastro.append(pessoa)
        print("Pessoa cadastrada com sucesso!")
    elif opcao == "2":
        if not cadastro:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in cadastro:
                print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Número da CTPS: {pessoa['num_ctps']}, Ano de Contratação: {pessoa['ano_contratação']}, Salário: {pessoa['salario']}")
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")