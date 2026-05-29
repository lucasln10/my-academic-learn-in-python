import tkinter as tk
from tkinter import messagebox
import conect

root = tk.Tk()

def enviar():
    texto = entrada.get().strip()

    if texto == "":
        return

    # Mostra a mensagem no chat
    chat.config(state="normal")
    chat.insert(tk.END, f"Você: {texto}\n")

    # Resposta simples do bot
    chat.insert(tk.END, f"Bot: Você escreveu '{texto}'\n\n")

    chat.config(state="disabled")
    chat.see(tk.END)

    entrada.delete(0, tk.END)

root.title("Chat")
root.geometry("600x700")
root.resizable(False, False)
root.configure(bg="#464646")

label = tk.Label(
    root,
    text="Chat AI!",
    font=("Arial", 30),
    fg="white",
    bg="#464646"
)
label.pack(pady=10)

# Área de mensagens
chat = tk.Text(
    root,
    width=65,
    height=25,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 11)
)
chat.pack(pady=10)
chat.config(state="disabled")

# Frame para entrada + botão
frame = tk.Frame(root, bg="#464646")
frame.pack(pady=10)

entrada = tk.Entry(frame, width=45, font=("Arial", 12))
entrada.pack(side=tk.LEFT, padx=30)

btn_enviar = tk.Button(
    frame,
    text="Enviar",
    command=enviar,
    bg="#5cb85c",
    fg="white"
)
btn_enviar.pack(side=tk.LEFT)

entrada.bind("<Return>", lambda event: enviar())

root.mainloop()