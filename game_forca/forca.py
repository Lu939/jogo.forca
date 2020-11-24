from random import choice
tentativas = 6
letras_certas = list()
letras_erradas = list()
palavras = ('flamengo', 'vasco', 'botafogo', 'fluminense', 'sao paulo', 'corinthians', 'palmeiras', 'santos')
sorteada = str(choice(palavras)).upper()
print('======= JOGO DA FORCA =======')
print('==== TIMES RIO SÃO PAULO ====')
print('-=' * 30)
print(f'O time tem {len(sorteada)} letras e a letra {sorteada[2-1]} esta na segunda posição')
while tentativas <= 6:
    jogador = str(input(f'São {tentativas} tentativas, palpite uma letra\nTente acertar o time:')).strip().upper()
    tentativas -= 1
    print('-=' * 30)
    if jogador in sorteada:
        letras_certas.append(jogador)
    else:
        letras_erradas.append(jogador)
    print(f'{letras_certas} são as letras corretas\n{letras_erradas} são as erradas')
    arriscar = str(input('Quer arriscar o nome? [SIM/NÃO]')).strip().upper()[0]
    if arriscar == 'S':
        vida_morte = str(input('Qual é o nome no time?')).strip().upper()
        if vida_morte == sorteada:
            print('PARABÉNS!!! VOCÊ VENCEU!!')
        else:
            print(f'PERDEU o time era {sorteada}')
            break
    if tentativas == 0:
        break
print(f'Fim\n{sorteada} foi o time! ')