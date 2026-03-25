from Person import Person

class Account(Person):
    def __init__(self, id, name, age, email, password, salario, saldo=0):
        super().__init__(id, name, age, email, password)
        self.salario = salario
        self.saldo = saldo
        self.account = []

    def saveAccount(self):
        account_data = {
            "id": self.id,
            "salario": self.salario,
            "saldo": self.saldo
        }
        self.account.append(account_data)

    def savePerson(self, id, name, age, email, password):
        super().savePerson(id, name, age, email, password)

    def getAllAccount(self, id):
        accountExist = ""
        for account in self.account:
            if id == account["id"]:
                accountExist = account
        if not accountExist:
            print("conta não existe")

        return None    