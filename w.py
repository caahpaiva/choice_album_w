from random import choice

albums = ['Wanessa Camargo 2000',
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
          'Livre']

def sorteio(albums):
    return choice(albums)

name = input('Olá, digite o seu nome: ')
print(f'\n======= Olá, {name}! Qual álbum da Wanessa Camargo vamos escutar hoje? =======')

def menu_inicial():
    while True:
        try:
            escolha = int(input('\nDigite o número 1 para sortear um álbum ou 2 para finalizar: '))
            if escolha in [1, 2]:
                return escolha
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

while True:
    sortear = menu_inicial()

    if sortear == 1:
        while True:
            escutar = sorteio(albums)
            print(f'\nO álbum sorteado para escutar hoje é: {escutar}')

            try:
                resposta = int(input('\nDeseja realizar um novo sorteio? Digite 1 para SIM ou 2 para NÃO: '))
                if resposta == 1:
                    continue
                elif resposta == 2:
                    print("Concluído! Até a próxima :)")
                    exit()  # <- Encerra o programa completamente
                else:
                    print("Opção inválida. Digite 1 ou 2.")
            except ValueError:
                print("Por favor, digite um número válido.")
    elif sortear == 2:
        print("Concluído! Até a próxima :)")
        break