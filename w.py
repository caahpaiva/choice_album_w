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
    escutar = choice(albums)
    return escutar

name = input(f'Olá, digite o seu nome: ')
print(f' \n ======= Olá, {name}! Qual álbum da Wanessa Camargo vamos escutar hoje? =======')

def iniciar():
    sortear = int(input('\n Digite o número 1 para sortear um albúm: '))
    return sortear

sortear = iniciar()

if sortear == 1:
    escutar = sorteio(albums)
    print(f'\n O álbum sorteado para escutar hoje é: {escutar}')
else: 
    iniciar()



    


