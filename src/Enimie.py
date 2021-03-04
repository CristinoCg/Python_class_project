from random import randint
def numero_i():
    from random import randint
    m = randint(0,2)
    print(f'Números de inimgos:{m}')
    return m

def Ataque_personagem(v, el, dn, l):
    m = 0
    escolha = 0
    while v != 0:
        if dn == 0:
            print('Você não tem mais dinheiro.')
            break
        else:
            print(f'Você tem {dn} desponível')
            for c in range(0,4):
                print(f'Ataque{c+1}:{l[1][c]} / Dano:{l[0][c]} / Custo:{l[2][c]}\n')
            escolha = int(input('Ataque número:'))
            if escolha == 1:
                print(f'Você usou: {l[1][escolha-1]}')
                el -= l[0][escolha-1]
                dn -=  l[2][escolha-1]
                print(f'O inimigo tem {el} de vida')

            elif escolha == 2:
                print(f'Você usou: {l[1][escolha-1]}')
                el -= l[0][escolha-1]
                dn -=  l[2][escolha-1]
                print(f'O inimigo tem {el} de vida')
            elif escolha ==3:
                print(f'Você usou: {l[1][escolha-1]}')
                el -= l[0][escolha-1]
                dn -=  l[2][escolha-1]
                print(f'O inimigo tem {el} de vida')
            elif escolha == 4:
                print(f'Você usou: {l[1][escolha-1]}')
                el -= l[0][escolha-1]
                dn -=  l[2][escolha-1]
                print(f'O inimigo tem {el} de vida')
            else:
                print('Escolha indisponível.')
                break
        if  el != 0 and v != 0:
            enmvar = randint(0,3)
            v -= l[0][enmvar]
            print(f'O inimigo usou :{l[1][enmvar]}\n Sua vida atual é {v}')
        else:
            print('inimigo morto')
            break
        if v < 50:
            print('Sua vida está abaixo dos 50')
            print('Deseja Recuperar?')
            break
           
