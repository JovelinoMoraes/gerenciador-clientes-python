import os


# FUNÇAO QUE CADASTRA CLIENTES NOVOS
def cadastrar_clientes():
    while True:
        try:
            quantidade_clientes = int(input("Quantos clientes deseja cadastrar ?"))
            if quantidade_clientes <= 0:
                print("Digite um número maior que zero")
            else:
                break
        except ValueError:
            print("Entrada inválida, digite um numero maior que 0")

    clientes = []

    for i in range(quantidade_clientes):
        cliente = {}
        cliente["nome"] = input(f"Digite o nome do {i + 1}º cliente:  ").capitalize()
        while True:
            try:
                cliente["saldo"] = float(input(f"Digite o saldo do {i + 1}º cliente: "))
                break
            except ValueError:
                print("Saldo Inválido! Digite um numero")

        print(f"Cliente {cliente['nome']} cadastrado(a) com sucesso!")
        clientes.append(cliente)
    return clientes


# FUNÇÃO QUE SALVA O CLIENTE CADASTRADO EM UM ARQUIVO TXT
def salvar_em_arquivo(clientes):
    os.makedirs("../data", exist_ok=True)
    with open("../data/clientes.txt", "a", encoding="utf-8") as file:

        for cliente in clientes:
            linha = f"{cliente['nome']},{cliente['saldo']}\n"
            file.write(linha)
