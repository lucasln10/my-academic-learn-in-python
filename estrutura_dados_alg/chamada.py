from faker import Faker
import random

faker = Faker('pt_BR')

countStudents = 30
days = 30
chamadas = []
porcPresences = []
porcNotPresences = []

def calcPrecences():
    taxa_ausencia = (len(porcNotPresences) / countStudents) * 100
    taxa_presenca = (len(porcPresences) / countStudents) * 100
    return f"Taxa de presença das aulas é {taxa_presenca:.2f}% e taxa de ausencias é {taxa_ausencia:.2f}%"

def saveGets(aluno, response, day):    
    allGets = {
        "Student": aluno,
        "Frequency": {
            "day": day,
            "presences": response
        }
    }
    return allGets

def main():
    for i in range(countStudents):
        aluno = faker.name()
        for j in range(days):
            result = random.randint(0,1)
            chamadas.append(saveGets(aluno, result, j+1))
    for chamada in chamadas:
        if chamada["Frequency"]["presences"] == 0:
            porcNotPresences.append(chamada)
        else:
            porcPresences.append(chamada)

    print(calcPrecences())

main()