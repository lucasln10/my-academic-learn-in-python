import random

pesquisa_pessoas = 1000
alturas = []
maior = 0
menor = 0
media = 0

def getAltura():
        alturas.append(round(random.uniform(1, 1.98), 3))

for i in range(pesquisa_pessoas):
    getAltura()

for i in alturas:
      if i > maior:
            maior = i
      elif menor == 0:
           menor = i
      elif i < menor:
            menor = i
      media+=i
      
print(maior)
print(menor)
print(round(media/pesquisa_pessoas, 2))