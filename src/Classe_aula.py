#pt Este programa é um estudo sobre classes e tem um exemplo claro e básico de classe
#En This program is a study of classes and it has an example simple and easy of class


from Enimie import numero_i, Ataque_personagem
from random import randint
from time import sleep

class Heroi:

    def __init__(self, nome):
        self.nome = nome
        self.vivo = True
        self.vida = 300
        self.dinheiro_ataque = 6000

    

class Inimigo:
    vivo = True
    vida = 300

class Boss:
    vivo = True
    vida = 1000

    

lista = ((90,200,30,20),('Espada', 'Lança', 'Pedra', 'Soco'),(800, 1200, 500, 250))

print("""Pt: Este código é uma especie de simulação de um jogo para o entendimento de classes
O usuário possui um valor de 6000 para usar para comprar ataques, que serão usadas para lutar contra os inimigos.""")
print("""\nEn: This code is kinda simulation of a real game for classes understanding
The player has a value of 6000 to buy the attacks, that will be used for fight against the enimies.""")

idioma = int(input('ENGLISH[1]/PORTUGUÊS[2]:'))
inimigo1 = Inimigo()
inimigo2 = Inimigo()
inimigo2.vida = 500
boss = Boss()
listae = (inimigo1.vida, inimigo2.vida, boss.vida)

if idioma == 1:
    tate_no_yusha = Heroi(input('Write your name heroe:'))
    """while tate_no_yusha.vivo:
        print('Rato')"""
elif idioma == 2:
    tate_no_yusha = Heroi(input('Digite o seu nome heroi/heroina:'))
    while tate_no_yusha.vivo:
        numero_inim = numero_i()
        if numero_inim == 0:
            print(f'Não existem inimigos na área')
            sleep(2)
            print('Você está a salvo, por enquanto...')
            sleep(2)
        else:
            print(f'Existe {numero_inim} inimigo' if numero_inim == 1 else f'Existem {numero_inim} inimigos')
            if numero_inim == 1:
                eescolha = 0
                eescolha = randint(0,2)
                if eescolha == 2:
                    print('É um boss kkkkk')
                else:
                    print('Tipo de inimigo: Comum')
                Ataque_personagem(tate_no_yusha.vida, listae[eescolha], 6000, lista)
                break
            else:
                print('2 inimigos a caminho')
                print('Você lutará com dois inimigos, escolha com qual irá lutar primeiro')
                print(f'Vida do inimigo1{inimigo1.vida}\Vida do inimigo 2{inimigo2.vida}')
                eescolha = 0
                escolha = int(input('Inimigo[1/2]:')
                if eescolha == 1 or eeescolha == 2:
                              if eescolha == 1:
                                if inimigo1.vivo:
                                  Ataque_personagem(tate_no_yusha.vida, listae[eescolha], 6000, lista)
                              
                                
                                
                              else:
                
                    
               
                


        
        
    

