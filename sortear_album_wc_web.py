from pywebio.input import *
from pywebio.output import *
from random import choice
from pywebio.platform.replit import start_server

# Lista de álbuns
albums = [
    'Wanessa Camargo 2000', 'Wanessa Camargo 2001', 'Wanessa Camargo 2002',
    'Transparente', 'W', 'Total', 'Meu Momento', 'DNA', 'DNA ao vivo', '33',
    'Universo Invertido', 'Pai e Filha', 'Livre'
]

# Função principal do app
def app():
    put_html("<h2 style='text-align:center;'>🎤 Sorteador de Álbuns - Wanessa Camargo</h2>")

    # Imagem no topo
    try:
        img_src = "/wanessa.jpg"  # Caminho da imagem no Replit
        put_html(f"<div style='text-align:center'><img src='{img_src}' width='200'></div><br>")
    except Exception as e:
        put_warning(f"Erro ao carregar imagem: {e}")

    name = input("Qual o seu nome?")
    put_text(f"Olá, {name}! Vamos escolher um álbum para escutar hoje?")

    sorteados = []

    while True:
        acao = actions(label="Escolha uma opção:", buttons=["🎲 Sortear Álbum", "🚪 Sair"])

        if acao == "🎲 Sortear Álbum":
            restantes = [a for a in albums if a not in sorteados]
            if not restantes:
                put_success("✅ Todos os álbuns já foram sorteados!")
                break
            escolhido = choice(restantes)
            sorteados.append(escolhido)
            put_markdown(f"### 🎧 Álbum sorteado:\n**{escolhido}**")
        else:
            put_text("Até logo! Obrigado por usar o sorteador. 💚")
            break

# Iniciar o servidor
if __name__ == "__main__":
    start_server(app)
