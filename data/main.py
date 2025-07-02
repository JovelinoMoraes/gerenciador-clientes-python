from logging import exception


def menu():
    while True:
        print("""
        ----- MENU ----
        1 - Cadastrar cliente
        2 - Mostrar todos os clientes
        3 - Mostrar clientes com saldo negativo
        4 - Mostrar cliente com maior saldo
        5 - Sair""")
        try:
            resposta = int(input(" Escolha uma opçã: "))
            if 1 <= resposta <= 5:
                return resposta
        else:
        print("Entrada inválida, escolha um numero de 1 a 5")
        except ValueError:
            print("Entrada inválida, escolha um numero de 1 a 5")


menu()