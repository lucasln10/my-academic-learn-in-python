pilha = []
counter = 0

while counter < 10:
    resp = input("Digite um valor ")
    pilha.append(resp)
    counter += 1
    
for i in range(len(pilha)):
    print("Valor: ", pilha[i])
    

    
