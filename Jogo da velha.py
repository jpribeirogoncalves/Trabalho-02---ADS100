

import random 
sorteio = random.randrange(1, 10) 
vez =  'X' 
j =''
p1 = '1' 
p2 = '2'
p3 = '3'
p4 = '4'
p5 = '5'
p6 = '6'
p7 = '7'
p8 = '8'
p9 = '9'
def tabuleiro(): 
    print('-----------------')
    print (p1, ' |', p2,'|', p3)
    print ('---|---|---')
    print (p4, ' |', p5, '|', p6)
    print ('---|---|---')
    print (p7, ' |', p8, '|', p9)
    print('-----------------')
    
def ganhador(p1, p2, p3, p4, p5, p6, p7, p8, p9): 
    return p1 == p2 == p3 or p4 == p5 == p6 or p7 == p8 == p9 or \
       p1 == p4 == p7 or p2 == p5 == p8 or p3 == p6 == p9 or \
       p1 == p5 == p9 or p3 == p5 == p7 
        


def deu_velha(p1, p2, p3, p4, p5, p6, p7, p8, p9): 
      return p1 != '1' and p2 != '2' and p3 != '3' and \
        p4 != '4' and p5 != '5' and p6 != '6' and \
        p7 != '7' and p8 != '8' and p9 != '9' 

def valida_casa(p, p1, p2, p3, p4, p5, p6, p7, p8, p9): 
    if p1 == '1':
            return True
    elif p  == '2':
        if p2 == '2':
            return True
    elif p == '3':
        if p3 =='3':
            return True
    elif p =='4':
        if p4=='4':
            return True
    elif p == '5':
        if p5 == '5' :
            return True
    elif p =='6':
        if p6 == '6':
            return True
    elif p == '7':
        if p7 == '7':
            return True
    elif p == '8':
        if p8 == '8':
            return True
    elif p == '9':
        if p9 == '9':
            return True
    return False        


def jogar():

    global vez, p1, p2, p3, p4, p5, p6, p7, p8, p9, computador

    if computador and vez == 'O':
        jogo = str(random.randrange(1, 10))
        while  not valida_casa(jogo ,p1, p2, p3, p4, p5, p6, p7, p8, p9):
           jogo = str(random.randrange(1, 10))
        print('Eu joguei no', jogo) 
    else:
        jogo = str(input('\nDigite a posição da sua jogada (1 a 9): ')) 
        while  not valida_casa(jogo ,p1, p2, p3, p4, p5, p6, p7, p8, p9): 
            print('Jogada invalida') 
            jogo = str(input('\nDigite a posição da sua jogada (1 a 9): '))


    if jogo == p1: 
        p1 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == p2:
        p2 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == p3:
        p3 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == p4:
        p4 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == p5:
        p5 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == p6:
        p6 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == p7:
        p7 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == p8:
        p8 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == p9:
        p9 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    print('Agora é a vez de', vez)
    
    
jogando = True
computador = False
while jogando:
    print('---------------------------------')
    computador = str(input('Ousas me desafiar?? (Digite 1 para sim / Digite 2 para não) ')) == '1' 
    if computador:
        print('---------------------------------')
        print("\nVocê ficara com o 'X' (xis)")
        print("\nE eu ficarei com o 'O' (bolinha)")
        print('---------------------------------')
        jogador1= input('\nDigite seu nome: ') 
    else:
        print ('\nInforme o nome de cada jogador')
        jogador1= input('\nDigite o nome do Jogador 1 (X): ') 
        jogador2 = input('\nDigite o nome do Jogador 2 (O): ')
    if computador == True:
        print("\nOlá", jogador1,"vai ser uma honra jogar contra você.")
    while not deu_velha(p1, p2, p3, p4, p5, p6, p7, p8, p9) and \
     not ganhador(p1, p2, p3, p4, p5, p6, p7, p8, p9):
        tabuleiro()
        jogar()
    else: 
        tabuleiro()
        if ganhador(p1, p2, p3, p4, p5, p6, p7, p8, p9):
            if computador == False:
                if vez == "O":
                    vez = jogador1
                elif vez == "X":
                    vez = jogador2
                print('---------------------------------')
                print('Parabéns', vez, 'você mereceu essa vitória!')
                print('---------------------------------')
            if computador == True:
                if vez == "O":
                    vez = "X"
                    print('---------------------------------')
                    print('Aff, parabéns', jogador1, 'você mereceu essa vitória!')
                    print('---------------------------------')
                else:
                    print('---------------------------------')
                    print('Hahahaha respeita o PAI!!! Eu disse que você não ganhava de mim u.u') 
                    print('---------------------------------')
        else:
            print("Vish!! Deu velha ...")
        jogando  = input('Revanche? Ou vai peidar?? (Digite 1 para jogar novamente / Digite 2 para sair): ') == '1'
        if jogando:
            vez =  'X'
            j =''
            p1 = '1'
            p2 = '2'
            p3 = '3'
            p4 = '4'
            p5 = '5'
            p6 = '6'
            p7 = '7'
            p8 = '8'
            p9 = '9'
        else:
            print('---------------------------------')
            print('Nós, João Pedro, Alexandre Duarte e Pedro Lucas')
            print('Agradecemos você por jogar conosco!!')
            print('---------------------------------')