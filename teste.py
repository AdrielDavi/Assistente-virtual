import random        #OPONENTE É O X
x = 0
jogo = ["N","N","N","N","N","N","N","N","N"]
ojog = [0,1,2,3,4,5,6,7,8]
while True: 
    joga = random.choice(ojog)  #OPONENTE
    ojog.remove (joga)  #Posição já usada
    jogo[joga] = "X"
    print(jogo[0]+" "+jogo[1]+" "+jogo[2]+"\n"+jogo[3]+" "+jogo[4]+" "+jogo[5]+"\n"+jogo[6]+" "+jogo[7]+" "+jogo[8])
    joga2 = int(input("faça tua jogada: "))
    ojog.remove (joga2)
    
    jogo[joga2] = "O"
    
    #vitória do oponente:

    if jogo[0] == "X" and jogo[1] == "X" and jogo[2] == "X":
        print("Oponente ganhou")
        break
    if jogo[3] == "X" and jogo[4] == "X" and jogo[5] == "X":
        print("Oponente ganhou")
        break
    if jogo[6] == "X" and jogo[7] == "X" and jogo[8] == "X":
        print("Oponente ganhou")
        break
    if jogo[0] == "X" and jogo[3] == "X" and jogo[6] == "X":
        print("Oponente ganhou")
        break
    if jogo[1] == "X" and jogo[4] == "X" and jogo[7] == "X":
        print("Oponente ganhou")
        break
    if jogo[2] == "X" and jogo[5] == "X" and jogo[8] == "X":
        print("Oponente ganhou")
        break
    if jogo[0] == "X" and jogo[4] == "X" and jogo[8] == "X":
        print("Oponente ganhou")
        break
    if jogo[2] == "X" and jogo[4] == "X" and jogo[6] == "X":
        print("Oponente ganhou")
        break

    #vitória:

    
    if jogo[0] == "O" and jogo[1] == "O" and jogo[2] == "O":
        print("Você ganhou")
        break
    if jogo[3] == "O" and jogo[4] == "O" and jogo[5] == "O":
        print("Você ganhou")
        break
    if jogo[6] == "O" and jogo[7] == "O" and jogo[8] == "O":
        print("Você ganhou")
        break
    if jogo[0] == "O" and jogo[3] == "O" and jogo[6] == "O":
        print("Você ganhou")
        break
    if jogo[1] == "O" and jogo[4] == "O" and jogo[7] == "O":
        print("Você ganhou")
        break
    if jogo[2] == "O" and jogo[5] == "O" and jogo[8] == "O":
        print("Você ganhou")
        break
    if jogo[0] == "O" and jogo[4] == "O" and jogo[8] == "O":
        print("Você ganhou")
        break
    if jogo[2] == "O" and jogo[4] == "O" and jogo[6] == "O":
        print("Você ganhou")
        break
    





    x = x +1
    if x == 8:
        print("Empate")
        break
   
