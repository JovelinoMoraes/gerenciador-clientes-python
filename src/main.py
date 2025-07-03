from cadastro import *
from relatorios import *

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
            opcao = int(input(" Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida, escolha um numero de 1 a 5")
            continue
        match opcao:
            case 1:
                clientes = cadastrar_clientes()
                salvar_em_arquivo(clientes)
            case 2:
                mostrar_todos_clientes()
            case 3:
                mostrar_clientes_negativos()
            case 4:
                mostrar_cliente_maior_saldo()
            case 5:
                print("SAINDO DO SISTEMA...")
                break
            case _:
                print("Opção inválida! Escolha um numero de 1 a 5")


menu()
