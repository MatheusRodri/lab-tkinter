import tkinter as tk
from tkinter import messagebox, simpledialog,filedialog


# # Mostrar uma mensagem de boas-vindas
# messagebox.showinfo("Sucesso", "Bem-vindo ao Tkinter!")

# # Solicitar o nome do usuário
# nome = simpledialog.askstring("Entrada", "Qual é o seu nome?")

# # Exibir uma saudação personalizada
# messagebox.showinfo("Saudação", f"Olá, {nome}! Seja bem-vindo ao Tkinter!")


arquivo = filedialog.askopenfilename(
    title="Selecione a base de dados",
    filetypes=[("Arquivos CSV", "*.csv"), ("Arquivos de texto", "*.txt")]
)

print(f"Arquivo selecionado: {arquivo}")
