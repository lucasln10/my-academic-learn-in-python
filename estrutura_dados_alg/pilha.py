pilha = []
valid = True

while valid:
    resp = input("Digite um valor ")
    pilha.append(resp)
    option = input("Quer para?\n1 - SIM\n2 - NÃO\nR: ")
    if option == 1:
        valid = True
    else:
        valid = False    
    