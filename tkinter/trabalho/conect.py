import socket
import threading

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("localhost", 8080))
threading.Thread(target=mostrarMSG, daemon=True).start()

def enviarMSG(message):
    cliente.send(message + "\n")

def mostrarMSG():
    return cliente.recv(1024).decode("utf-8")