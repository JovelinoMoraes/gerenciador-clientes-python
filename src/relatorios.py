from os.path import split
import os


def valida_arquivo():
    caminho_arquivo = "../data/clientes.txt"

    if not os.path.exists(caminho_arquivo):
        print("⚠️ Lista de clientes não encontrada.")
        return False

    if os.path.getsize(caminho_arquivo) == 0:
        print("⚠️ Nenhum cliente cadastrado ainda.")
        return False

    return True


# FUNÇÃO QUE MOSTRA TODOS OS CLIENTES CADASTRADOS
def mostrar_todos_clientes():
    if not valida_arquivo():
        return
    with open("../data/clientes.txt", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        print(" ---- Lista de Clientes ----")
        for linha in linhas:
            nome, saldo = linha.strip().split(",")
            saldo = float(saldo)
            if saldo < 0:
                print(f"{nome:<10} - R$ {saldo:7.2f} ⚠️ Saldo Negativo")
            else:
                print(f"{nome:<10} - R$ {saldo:7.2f}")
        print("----------------------------")


# FUNÇÃO QUE MOSTRA APENAS OS CLIENTES COM SALDO NEGATIVO
def mostrar_clientes_negativos():
    if not valida_arquivo():
        return
    with open("../data/clientes.txt", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        print(" ---- Lista de Clientes Negativados ----")
        for linha in linhas:
            nome, saldo = linha.strip().split(",")
            saldo = float(saldo)
            if saldo < 0:
                print(f"{nome:<10} - R$ {saldo:7.2f} ⚠️ Saldo Negativo")
        print("----------------------------")


#  FUNÇÃO QUE MOSTRA O CLIENTE COM MAIOR SALDO
def mostrar_cliente_maior_saldo():
    if not valida_arquivo():
        return
    with open("../data/clientes.txt", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        print(" ---- Cliente com o maior saldo  ----")
        max_saldo = float("-inf")
        max_nome = ""
        for linha in linhas:
            nome, saldo = linha.strip().split(",")
            saldo = float(saldo)

            if saldo > max_saldo:
                max_saldo = saldo
                max_nome = nome
    print(f"cliente com maior saldo: {max_nome} , e seu saldo é R$ {max_saldo:.2f}")
