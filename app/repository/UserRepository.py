import entity.User

user = entity.User
banco = user.banco
cursor = user.cursor

def create(name, idade, email):
    sql = f"INSERT INTO users(nome, idade, email) VALUES('{name}', {idade}, '{email}')"
    cursor.execute(sql)
    banco.commit()

def update(id, name, idade, email):
    update = f"UPDATE users SET nome = '{name}', idade = {idade}, email = '{email}' WHERE id = {id}"
    cursor.execute(update)
    banco.commit()

def delete(id):
    delete = f"DELETE FROM users WHERE id = {id}"
    cursor.execute(delete)
    banco.commit()

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