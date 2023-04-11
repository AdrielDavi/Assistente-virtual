import random
import pygame #parte gráfica
from pygame import mixer
from pygame.locals import *
import sys #uso para sair do programa
from sys import exit #uso para sair do programa
from datetime import date #dar Datas
import speech_recognition as sr #fala
import cv2  #nem lembro
import pytesseract #ler imagens
import pyscreenshot #tirar  print 
import os # executa comandos do terminal
import pyttsx3 #tem função de ler txt e pdf
import threading #multiprocessamento
import pyautogui #auto


#Funções:


def audio(texto): #fala o texto além de ser responsável pela velocidade da fala
    speaker = pyttsx3.init() #inicia a biblioteca
    voices = speaker.getProperty("voices") #sei lá
    rate = speaker.getProperty("rate") # SL
    speaker.setProperty("rate",confirma2) # velocidade
    #speaker.setProperty("voice", voices[3].id) #voz 0,1,2,3 .... homem ou mulher
    speaker.say(texto) #define o texto que será lido
    speaker.runAndWait() #le o texto
def ouvir_microfone(): #Retorna a frase que eu disser
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) #abafa o barulho ambiente
        print("Diga alguma coisa: ")
        tela.blit(apaga,(250,350)) #legenda
        img = font.render('Diga alguma coisa', True, (255,255,255),(0,0,0)) #legenda
        tela.blit(img, (250,350)) #legenda
        audio = microfone.listen(source) #escuta seu microfone 
    try:
        frase = microfone.recognize_google(audio,language='pt-BR') #decifra o que você disse
        print("Você disse: " + frase)
        tela.blit(apaga,(250,350)) #legenda
        img = font.render("Você disse: " + frase, True, (255,255,255),(0,0,0)) #legenda
        tela.blit(img, (250,350)) #legenda
    except sr.UnknownValueError: #caso dê erro/ não entenda
        print("Não entendi")
        tela.blit(apaga,(250,350)) #legenda
        img = font.render('Não entendi', True, (255,255,255),(0,0,0)) #legenda
        tela.blit(img, (250,350)) #legenda
        frase = ""   #renicia a frase
    return frase

def fala_data (x): #retorn a data toda junta
    retorna = ""
    for i in x:
        if i != "/":
            retorna = retorna + i
    return retorna  

def pupila (): #código do pupila
    global confirma_inicio #A variavél passa a interagir com o pygame
    
    
    while True:
        comando_invalido = 0
        piadas=["O que o pato disse para a pata? Vem Quá!", "Porque o menino estava falando ao telefone deitado? Para não cair a ligação","Qual é a fórmula da água benta?H Deus O!","Qual é a cidade brasileira que não tem táxi? Uberlândia","O que o tijolo falou para o outro? Há um ciumento entre nós."]   
        data_atual = date.today() #data atual (do computador pessoal)
        data_em_texto = data_atual.strftime("%d/%m/%Y") #converte para 
        frase = ouvir_microfone() #frase recebe a função "ouvir" que retorna a frase dita
        frase = frase.lower() #converta as letras do que foito em minúsculas
        mover = ""
        
        
        
        #ler a tela
        if frase == "pupila leia isso" or frase == "pupila por favor leia isso" or frase == "pupila leia isto" or frase == "pupila por favor leia isto" or frase == "pupila ler isso" or frase == "pupila por favor ler isso" or frase == "pupila leia isto" or frase == "pupila por favor ler isto" or frase == "pupila ler isso aqui" or frase == "pupila leia isso para mim" or frase == "pupila ler isto pra mim" or frase == "pupila ler isto parra mim": #ler a tela
            comando_invalido = 1
            imagem = pyscreenshot.grab() #tira o print
            imagem.save("tela.png") # Salva com o nome tela
            img = cv2.imread("tela.png") #ler a imagem
            pytesseract.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe") #caminho
            resultado = pytesseract.image_to_string(img) #Converte a imagem para string
            print (resultado)
            audio(resultado)
        #NAVEGAR (relacionado ao pc em si)
        if frase == "pupila abrir gerenciador de tarefas" or frase == "pupila abrir o gerenciador de tarefas" or frase == "pupila abra o gerenciador de tarefas":
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Abrindo o Google', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Abrindo o gerenciador de tarefas")
            os.system("start taskmgr.exe") 
        if frase == "pupila fechar gerenciador de tarefas" or frase == "pupila fechar o gerenciador de tarefas" or frase == "pupila feche o gerenciador de tarefas": #fecha o google
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('fechando o gerenciador de tarefas', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("fechando o gerenciador de tarefas")
            os.system("taskkill /f /im taskmgr.exe")

        if frase == "pupila abrir pasta" or frase == "pupila abrir a pasta" or frase == "pupila abra a pasta para mim":
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Abrindo pasta', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Abrindo pasta")
            os.system("start explorer.exe") 
        if frase == "pupila fechar pasta" or frase == "pupila fechar a pasta" or frase == "pupila feche a pasta": #fecha o google
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('fechando pasta', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Sem permissão")
            

        if frase == "pupila abrir bloco de notas" or frase == "pupila abrir o bloco de notas" or frase == "pupila abra o bloco de notas":
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Abrindo bloco de notas', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Abrindo bloco de notas")
            os.system("start notepad.exe") 
        if frase == "pupila fechar bloco de notas" or frase == "pupila fechar o bloco de notas" or frase == "pupila feche o bloco de notas": #fecha o google
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('fechando bloco de notas', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("fechando bloco de notas")
            os.system("taskkill /f /im notepad.exe") 

        if frase[0:14] == "pupila escreva" or frase[0:13] == "pupila digite": #escreve qualquer coisa        #COLOCAR O DIGITE
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Escrevendo...', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Escrevendo")
            pyautogui.write(frase[15::])

        if frase == "pupila enter" or frase == "pupila confirmar" or frase == "pupila pressione enter" or frase == "pupila pressione o botão enter":
            pyautogui.press("enter")

        #MOUSE
        if frase[0:15] == "pupila esquerda":
            comando_invalido = 1
            mover = ""
            for i in frase:
                if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
                    mover = mover + i
            mover = int(mover) 
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX - mover, currentMouseY)

        if frase[0:14] == "pupila direita":
            comando_invalido = 1
            mover = ""
            for i in frase:
                if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
                    mover = mover + i
            mover = int(mover) 
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX + mover, currentMouseY)

        if frase[0:11] == "pupila cima":
            comando_invalido = 1
            mover = ""
            for i in frase:
                if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
                    mover = mover + i
            mover = int(mover) 
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX , currentMouseY - mover)

        if frase[0:12] == "pupila baixo":
            comando_invalido = 1
            mover = ""
            for i in frase:
                if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
                    mover = mover + i
            mover = int(mover) 
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX + mover, currentMouseY + mover)

        if frase == "pupila clique" or frase == "pupila clicar" or frase == "pupila clique para mim": #clica
            comando_invalido = 1
            pyautogui.click() 

        

        
        

        



        #NAVEGAR (tudo que envolver navegador) [lembrar de colocar uma opção abrir navegador padrão]
        if frase[0:21] == "pupila pesquise sobre": #Pesquisa o que você quiser   #ADICIONAR MAIS FALAS
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Pesquisando sobre'+frase[22::], True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio('Pesquisando sobre'+frase[22::])
            os.startfile("https://www.google.com/search?q="+frase[22::])
        
        if frase[0:26] == "pupila quantos dias faltam": #Pesquisa o que você quiser
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Pesquisando sobre', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio('Pesquisando sobre')
            os.startfile("https://www.google.com/search?q="+frase[27::])

        

        
        if frase == "pupila abrir google" or frase == "pupila abrir o google" or frase == "pupila abra o google" or frase == "pupila abra o google para mim":
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Abrindo o Google', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Abrindo o Google")
            os.system("start chrome") 
        if frase == "pupila fechar google" or frase == "pupila fechar o google" or frase == "pupila feche o google": #fecha o google
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('fechando o Google', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("fechando o Google")
            os.system("taskkill /f /im chrome.exe") 

        if frase == "pupila abrir youtube":
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Abrindo o Youtube', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Abrindo o YouTube")
            os.startfile("https://www.youtube.com/")
        if frase == "pupila fechar youtube" or frase == "pupila fechar o youtube": #fecha o google
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('fechando o Youtube', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("fechando o Youtube")
            os.system("taskkill /f /im chrome.exe") 

        if frase == "pupila abrir música relaxante" or frase == "pupila coloque música relaxante" or frase == "pupila coloque uma música relaxante":
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Colocando músicas relaxantes', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("colocando músicas relaxantes")
            os.startfile("https://www.youtube.com/watch?v=pWjmpSD-ph0")
        #DATA (tudo relacionado a datas )
        if frase == "pupila qual a data de hoje":  #DATA ATUAL
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render("A data atual é " + fala_data(data_em_texto[0:2]) + " do " + fala_data(data_em_texto[3:5]) + " de " + fala_data(data_em_texto[6:10]), True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("A data atual é " + fala_data(data_em_texto[0:2]) + "do" + fala_data(data_em_texto[3:5]) + "de" + fala_data(data_em_texto[6:10]))          
        if frase == "pupila em que ano estamos": #ANO
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render("O ano atual é  " + fala_data(data_em_texto[6:10]), True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("O ano atual é " + fala_data(data_em_texto[6:10]))   
        if frase == "pupila em que mês estamos":  #MÊS (COLOCAR O NOME DO MÊS)
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render("O mês atual é " + fala_data(data_em_texto[3:5]) , True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("O mês atual é " + fala_data(data_em_texto[3:5]) )   
        if frase == "pupila que dia é hoje":  #DIA (COLOCAR SEGUNDA,terça)
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render("Hoje é dia " + fala_data(data_em_texto[0:2]) , True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Hoje é dia " + fala_data(data_em_texto[0:2]))   
        #Tumor
        if frase == "pupila me conte uma piada":
            comando_invalido = 1
            audio("Bom, você pediu, "+random.choice(piadas)) 
        #FIM
        if frase == "Sair do pupila" or frase == "sair do pupila" :
            comando_invalido = 1
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Adeus', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Adeus")
            confirma_inicio = 0 #Serve para rodar o pupila novamente
            break
        if comando_invalido == 0:
            tela.blit(apaga,(250,350)) #legenda
            img = font.render('Por favor, diga um comando válido', True, (255,255,255),(0,0,0)) #legenda
            tela.blit(img, (250,350)) #legenda
            audio("Por favor, diga um comando válido")
      
def iniciar_pupila(): #inia o pygame e o pupila em processamentos diferentes
    t = threading.Thread(target = pupila) #Deve torrar um processador se colocar mais de um desse
    t.start() #CUIDADO PERIGO cAVEIRA
    
def restart_program(): #Serve para fechar o pupila através de um erro no código (gambiarra)
    python = sys.executable
    os.execl(python, python, * sys.argv)
#PYGAME
pygame.init() #iniciar o pygame
pygame.display.set_caption("Pupila") #Título do programa
#Imagens
pupilaf = pygame.image.load("pupilaf.png") #logo do pupila
biniciar = pygame.image.load("biniciar.png") #Botão iniciar padrão (Pupila desligado)
biniciar2 = pygame.image.load("biniciar2.png") #Botão para quando o mouse fica por cima
biniciar3 = pygame.image.load("biniciar3.png") # Como o botão fica quando o pupila está rodando
menuham = pygame.image.load("menuham.png") # Menu hamburguér
menu_config1 = pygame.image.load("menu_config1.png") #Menu que aparece quando clica no hamburguér
vel_05 = pygame.image.load("vel_05.png") #velocidade x0.5
vel_normal = pygame.image.load("menu_normal.png") #velocidade padrão
vel_15 = pygame.image.load("vel_15.png") #velocidade x1.5
apaga = pygame.image.load("apaga.png") #atualiza a legenda (gambiarra)
#SOM

#tamanho da janela do Pupila
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
#Cores 
cinza = (107, 107, 107)
#variaveis no programa
botao_y = 0 # Confirma se o mouse está por cima do botão
confirma1 = 0 #confirma se o menu config está apertado
confirma2 = 200 #CONFIGURAÇÃO DE VELOCIDADE 100 = DEVAGAR; 200 = PADRÃO; RÁPIDO = 400
confirma_inicio = 0 #Confirma se apenas um pupila está rodando, se aperta o botão de novo automáticamente o fecha

#pygame
clock = pygame.time.Clock() #fps
font = pygame.font.SysFont(None, 24) #Fonte da legenda
while True:
    clock.tick(60) #60 fps
    
    for event in pygame.event.get():  
                
        #Sair
        if event.type == QUIT: #quando apertar no x sair do programa (gambiarra)
            restart_program()#gambiarra
            pygame.quit()
            exit()
            
        #imagens da tela
        tela.fill(cinza) #co de fundo do pupila
        tela.blit(pupilaf,(75,0)) #logo do pupila (provalvelmente está desalinhado)
        tela.blit(biniciar,(295,375))#botão  (provalvelmente está desalinhado)
        tela.blit(menuham,(0,0))#menu hamburguer
        if confirma1 != 0: # enquanto a confirmação for diferente de 0 o menu continuara aparecendo
            tela.blit(menu_config1,(440,160)) #menu de configuração

        #configurações do mouse:

        mx, my = pygame.mouse.get_pos() #Pega a a posição do mouse
       
        if confirma_inicio == 1:
            tela.blit(biniciar2,(295,375))#botão
        else:
            tela.blit(biniciar,(295,375))#botão

        #if para mudar o botão de  iniciar o pupila
        if mx >= 295 and mx <= 365 and my >= 374 and my <= 447 : #quando o mouse fica por cima o botão muda
            tela.blit(biniciar3,(295,375))#botão
        #if para abrir o menu config
        if event.type == MOUSEBUTTONDOWN:
            
            if mx >= 0 and mx <= 60 and my >= 0 and my <= 40 :
                mx, my = pygame.mouse.get_pos() #Pega a a posição do mouse
                tela.blit(menu_config1,(440,160)) #menu_config1
                confirma1 = confirma1 +1 #serve para manter o menu aparecendo
            else:
                confirma1 = 0 #server para tirar o menu da tela
        
        if event.type == MOUSEBUTTONDOWN: #velocidade x0.5
            if mx >= 450 and mx <= 464 and my >= 190 and my <= 204  :
                mx, my = pygame.mouse.get_pos()
                tela.blit(vel_05,(440,160)) #seleciona a velocidade lenta
                confirma2 = 100 #velocidade lenta
        
        if event.type == MOUSEBUTTONDOWN: #velocidade padrão
            if mx >= 450 and mx <= 464 and my >= 238 and my <= 254  :
                mx, my = pygame.mouse.get_pos() #pega a posição do  mouse
                tela.blit(vel_normal,(440,160)) #seleciona a velocidade padrão
                confirma2 = 200 # Velociade padrão
        
        if event.type == MOUSEBUTTONDOWN: #velocidade x1.5
            if mx >= 450 and mx <= 464 and my >= 290 and my <= 304  :
                mx, my = pygame.mouse.get_pos()
                tela.blit(vel_15,(440,160)) #seleciona a velocidade rápida
                confirma2 = 400 #velocidade rápida

        #pupila
        if confirma_inicio == 0: #Serve para não ter mais de um pupila rodando
            if event.type == MOUSEBUTTONDOWN: 
                if mx >= 287 and mx <= 365 and my >= 374 and my <= 447 :   
                    confirma_inicio = 1 #isso quer dizer que um pupila está rodando                
                    tela.blit(biniciar3,(295,375))#botão  
                    som_inicia = mixer.Sound("som_inicio.wav")
                    som_inicia.set_volume(0.5)  
                    som_inicia.play()  
                          
                    iniciar_pupila() #perigo morte demônio coisa ruim crâmunhão

                     
                
                
            
    pygame.display.update() #Atualiza o  pygame (pupila parte gráfica)