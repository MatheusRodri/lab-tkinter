import tkinter as tk
from tkinter.font import Font

janela = tk.Tk()

janela.title("Sistema de cadastro de usuários")
janela.geometry("900x600")

# Cria o elemento
titulo = tk.Label(text="Sistema de cadastro de usuários", font=Font(size=22,weight="bold",family="Arial"))
titulo.pack(pady=(20,20))

titulo = tk.Label(text="Sistema de cadastro de usuários", font=Font(size=14,weight="normal",family="Arial"))
titulo.pack(pady=(20,20))





janela.mainloop()