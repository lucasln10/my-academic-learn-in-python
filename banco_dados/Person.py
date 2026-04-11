class Person():
    person = []
    def __init__(self, id, name, age, email, password):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.password = password
    
    def savePerson(self, id, name, age, email, password):
        person = {
            "id": id,
            "name": name,
            "age": age,
            "email": email,
            "password": password
        }
        Person.person.append(person)

    def getPeson(self, id):
        personExist = ""
        for person in self.person:
            if person["id"] == id:
                personExist = person
        
        if not personExist:
            print(f"pessoa com id {id}, não existe!")

        return None