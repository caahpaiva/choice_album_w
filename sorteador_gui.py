import sys
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from random import choice


# Função para carregar imagem
def resource_path(relative_path):
    """Ajusta o caminho para quando o programa for empacotado com PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Lista de álbuns
albums = [
    'Wanessa Camargo 2000',
    'Wanessa Camargo 2001',
    'Wanessa Camargo 2002',
    'Transparente',
    'W',
    'Total',
    'Meu Momento', 
    'DNA', 
    'DNA ao vivo', 
    '33',
    'Universo Invertido',
    'Pai e Filha', 
    'Livre'
]

# Função de sorteio
def sortear_album():
    if not albums:
        messagebox.showinfo("Fim", "Todos os álbuns já foram sorteados!")
        return
    album = choice(albums)
    albums.remove(album)  # Evita repetir
    resultado_label.config(text=f"🎶 Álbum sorteado:\n{album}", fg="green")

# Função para sair
def sair():
    janela.destroy()

# Criação da janela
janela = tk.Tk()
janela.title("Sorteador de Álbuns - Wanessa Camargo")
janela.geometry("400x500")
janela.configure(bg="#000000")

# === Adiciona imagem no topo ===
try:
    imagem = Image.open(resource_path("wanessa.jpg")) # Use o nome do seu arquivo aqui
    # imagem = Image.open("wanessa.jpg")  
    imagem = imagem.resize((200, 200))  # Redimensiona
    foto = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(janela, image=foto, bg="#000000")
    label_imagem.pack(pady=10)
except Exception as e:
    print("Erro ao carregar imagem:", e)


# Título
titulo = tk.Label(janela, text="Qual álbum da Wanessa Camargo\nvamos escutar hoje?", 
                  font=("Helvetica", 14, "bold"), bg="#000000", fg="#f9f9f9")
titulo.pack(pady=20)

# Label de resultado
resultado_label = tk.Label(janela, text="", font=("Helvetica", 12), bg="#000000")
resultado_label.pack(pady=10)

# Botões
btn_sortear = tk.Button(janela, text="🎲 Sortear Álbum", font=("Helvetica", 12), bg="#d1e7dd", command=sortear_album)
btn_sortear.pack(pady=5)

btn_sair = tk.Button(janela, text="🚪 Sair", font=("Helvetica", 12), bg="#f8d7da", command=sair)
btn_sair.pack(pady=5)

# Inicia a interface
janela.mainloop()