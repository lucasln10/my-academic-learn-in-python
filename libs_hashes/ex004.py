import secrets
import string
import hashlib

token = hashlib.sha256(usedforsecurity=True)
# print(token.hexdigest())

alfabeto = string.ascii_letters
senha_forte = "".join(secrets.choice(alfabeto) for i in range(200))
# print(senha_forte)

cores = ["azul", "verde", "vermelho"]
escolha = secrets.choice(cores)
# print(escolha)

senha_1 = "hershell"
senha_2 = "hershell"
comparador = secrets.compare_digest(senha_1, senha_2)
# print(comparador)


def gerar_id_secao():
    return secrets.token_hex(30)

id_user = 1

secao = gerar_id_secao()
print(f"user: {id_user} | secao: {secao}")