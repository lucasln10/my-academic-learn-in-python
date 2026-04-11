import conecction

cursor = conecction.cursor

def validateParans(nome, idade, email):
    if nome == None or idade == 0 or email == None: return False
    return True
    

def create(name, idade, email):
    if validateParans(name, idade, email): print("params invalidos")
    try:            
        create = f"INSERT INTO users(nome, idade, email) VALUES('{name}', {idade}, '{email}')"
        cursor.execute(create)
        conecction.banco.commit()
        print("Usuario criado com sucesso!\n")
    except:
        print("Erro ao adicionar usuario no banco de dados.\n")

def updateUser(id, name, idade, email):
    if validateParans(name, idade, email): print("params invalidos")
    try:            
        update = f"UPDATE users SET nome = '{name}', idade = {idade}, email = '{email}' WHERE id = {id}"
        cursor.execute(update)
        conecction.banco.commit()
        print("Usuario atualizado com sucesso!\n")
    except:
        print("Erro ao atualizar usuario no banco de dados.\n")

def deleteUser(id):
    if id == None:
        print("Id is null")
        return
    try:            
        delete = f"DELETE FROM users WHERE id = {id}" #AND name = {name} AND idade = {idade} AND email = {email}"
        cursor.execute(delete)
        conecction.banco.commit()
        print("Usuario deletado com sucesso!\n")
    except:
        print("Erro ao deletar usuario no banco de dados.\n")
        

def getAllUsers():
    script  = "SELECT * FROM users"
    cursor.execute(script)
    return cursor.fetchall()

def getByUserId(id):
    if id == None: return "id is null" 
    script = f"SELECT * FROM users WHERE id = {id}"
    cursor.execute(script)
    return cursor.fetchall()

def getByName(nome):
    if nome == None: return "nome is null"
    nomes = []
    script = f"SELECT * FROM users WHERE nome = {nome}"
    cursor.execute(script)
    nomes = cursor.fetchall()
    return nomes

def getByIdade(idade):
    if idade == None: return "idade is null"
    idades = []
    script = f"SELECT * FROM users WHERE idade = {idade}"
    cursor.execute(script)
    idades = cursor.fetchall()
    return idades

def getByEmail(email):
    if email == None: return "email is null"
    script = f"SELECT * FROM users WHERE idade = {email}"
    cursor.execute(script)
    return cursor.fetchall()

def allGets():
    whatParam = int(input("Gostaria de procurar os usuarios do banco usando o\n1 - ID\n2 - Nome\n3 - Idade\n 4 - Email?\nR:"))
    print("\n")
    if whatParam == 1:
        paramId = int(input("Digite o id que gostaria de buscar: "))
        print(getByUserId(paramId))
    elif whatParam == 2:
        paramNome = input("Digite o nome que gostaria de buscar: ")
        print(getByName(paramNome))
    elif whatParam == 3:
        paramIdade = int(input("Digite a idade que gostaria de buscar: "))
        print(getByIdade(paramIdade))
    elif whatParam == 4:
        paramEmail = input("Digite o email que gostaria de buscar: ")
        print(getByEmail(paramEmail))
    else:
        print("Nenhum para valido")

def options(option):
    if option == 1:
        nome = input("Qual seu nome? ")
        idade = int(input("Quantos anos voce tem? "))
        email = input("Digite seu email? ")
        create(nome, idade, email)
    elif option == 2:
        allGets()
    elif option == 3:
        id = int(input("Qual id do user que voce quer atualizar? "))
        nome = input("Qual o novo nome? ")
        idade = int(input("Qual a nova idade? "))
        email = input("Qual o novo email? ")
        updateUser(id, nome, idade, email)
    elif option == 4:        
        id = int(input("Qual id do user que voce quer deletar? "))
        deleteUser(id)
    else:
        print("OPÇÃO INVALIDA!")

def main():
    option = int(input("Agora voce consegue fazer consultas ao banco.\n1 - CREATE\n2 - READ\n2 - UPDATE\n4 - DELETE\nR: "))
    options(option)
        

main()