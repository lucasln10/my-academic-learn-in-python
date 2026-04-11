from Account import Account
from Person import Person

def cadastro():

    nome = input("digite seu nome: ")
    idade = input("digite sua idade: ")
    email = input("digite seu email: ")
    senha = input("digite sua senha: ")
    salario = input("digite seu salario: ")
    cliente = Account(next, nome, idade, email, senha, salario)

    cliente.saveAccount(cliente)

def showAll(id):
    print(f"Pessoa: {Person.getPeson(id)}")
    print(f"Conta: {Account.getAllAccount(id)}")

def Main():
    valid = True

    while valid:
        print("BEM VINDO AO BANCO\n\n")
        print("Escolha uma Opação: \n\n")
        print("1 - Cadastro\n")
        print("2 - Ver Cadastros\n")
        print("3 - SAIR\n")
        escolha = int(input("Digite: "))
        if escolha == 1:
            cadastro()
        elif escolha == 2:
            print("digite um id de usuario: ")
            id = int(input())
            showAll(id)
        else:
            valid = False
Main()
