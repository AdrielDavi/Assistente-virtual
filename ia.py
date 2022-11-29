import pygame
from pygame.locals import *
from sys import exit
from datetime import date
#from email import message
#from tkinter import dialog 
import speech_recognition as sr
import cv2
import pytesseract
import pyscreenshot 
import os
import pyttsx3 #tem função de ler txt e pdf

#bbox=(10,10,500,500) -- corta a tela do print
#variáveis

#funções
def audio(texto):
    speaker = pyttsx3.init() #inicia a biblioteca
    voices = speaker.getProperty("voices") #sei lá
    rate =speaker.getProperty("rate") # SL
    speaker.setProperty("rate", rate-0) # velocidade
    #speaker.setProperty("voice", voices[3].id) #voz 0,1,2,3 ....
    speaker.say(texto) #define o texto que será lido
    speaker.runAndWait() #le o texto


def ouvir_microfone(): #Retorna a frase que eu disser
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        print("Você disse: " + frase)
    except sr.UnknownValueError:
        print("Não entendi")
        frase = ""   
    return frase
#variáveis

#def pupila():
    while True:
        todays_date = date.today()    
        frase = ouvir_microfone()
        frase = frase.lower()
        if frase == "pupila leia isso":
            imagem = pyscreenshot.grab() #tira o print
            imagem.save("tela.png") # Salva com o nome tela
            img = cv2.imread("tela.png") #ler a imagem
            pytesseract.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe") #caminho
            resultado = pytesseract.image_to_string(img) #Converte a imagem para string
            print (resultado)
            audio(resultado)
        #NAVEGAR
        if frase == "pupila abrir google":
            audio("Abrindo o Google")
            os.system("start chrome")
        if frase == "pupila abrir youtube":
            audio("Abrindo o YouTube")
            os.startfile("https://www.youtube.com/")
        if frase == "pupila abrir música relaxante" or frase == "pupila coloque música relaxante" or frase == "pupila coloque uma música relaxante":
            audio("colocando músicas relaxantes")
            os.startfile("https://www.youtube.com/watch?v=pWjmpSD-ph0")
        #DATA
       
        if frase == "pupila qual a data de hoje":  #colocar audio
            audio("Data atual: ", todays_date)           #colocar audio
        if frase == "pupila em que ano estamos":  #colocar audio
            audio("Ano atual:", todays_date.year) #colocar audio
        if frase == "pupila em que mês estamos":  #colocar audio
            audio("Mês atual:", todays_date.month) #colocar audio
        if frase == "pupila que dia é hoje":  #colocar audio
            audio("Dia atual:", todays_date.day)#colocar audio
        #FIM
        if frase == "Sair do pupila" or frase == "sair do pupila" :
            audio("Adeus")
            break

pygame.init()
pygame.display.set_caption("Pupila")



#IMagens
pupilaf = pygame.image.load("pupilaf.png")
biniciar = pygame.image.load("biniciar.png")
biniciar2 = pygame.image.load("biniciar2.png") #mouse por cima
biniciar3 = pygame.image.load("biniciar3.png") # Clica
menuham = pygame.image.load("menuham.png") # abre o Menu
menu_config1 = pygame.image.load("menu_config1.png") # Clica



#tamanho
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
#Cores
cinza = (107, 107, 107)
#variaveis no programa
botao_x = 0 # confirma se apertou
botao_y = 0 # Confirma se o mouse está por cima do botão

#pygame
while True:
    for event in pygame.event.get():           
        #Sair
        if event.type == QUIT:
            pygame.quit()
            exit()
        #imagens da tela
        tela.fill(cinza)
        tela.blit(pupilaf,(75,0)) #pupila
        tela.blit(biniciar,(282,375))#botão
        tela.blit(menuham,(0,0))#menu hamburguer
        

        #configurações do mouse
        mx, my = pygame.mouse.get_pos() #Pega a a posição do mouse
        if mx >= 287 and mx <= 365 and my >= 334 and my <= 456 :
            tela.blit(biniciar3,(282,375))#botão
        if event.type == MOUSEBUTTONDOWN:
            if mx >= 12 and mx <= 87 and my >= 12 and my <= 87 :
                mx, my = pygame.mouse.get_pos() #Pega a a posição do mouse
                tela.blit(menu_config1,(440,160)) #menu_config1
            
        
        
        #pupila
        if event.type == MOUSEBUTTONDOWN:
            
            mx, my = pygame.mouse.get_pos() #Pega a a posição do mouse
            if mx >= 287 and mx <= 365 and my >= 334 and my <= 456 :
                tela.blit(biniciar3,(282,375))#botão
                while True:
                    todays_date = date.today()    
                    frase = ouvir_microfone()
                    frase = frase.lower()
                    if frase == "pupila leia isso":
                        imagem = pyscreenshot.grab() #tira o print
                        imagem.save("tela.png") # Salva com o nome tela
                        img = cv2.imread("tela.png") #ler a imagem
                        pytesseract.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe") #caminho
                        resultado = pytesseract.image_to_string(img) #Converte a imagem para string
                        print (resultado)
                        audio(resultado)
                    #NAVEGAR
                    if frase == "pupila abrir google":
                        audio("Abrindo o Google")
                        os.system("start chrome")
                    if frase == "pupila abrir youtube":
                        audio("Abrindo o YouTube")
                        os.startfile("https://www.youtube.com/")
                    if frase == "pupila abrir música relaxante" or frase == "pupila coloque música relaxante" or frase == "pupila coloque uma música relaxante":
                        audio("colocando músicas relaxantes")
                        os.startfile("https://www.youtube.com/watch?v=pWjmpSD-ph0")
                    #DATA
       
                    if frase == "pupila qual a data de hoje":  #colocar audio
                        audio("Data atual: ", todays_date)           #colocar audio
                    if frase == "pupila em que ano estamos":  #colocar audio
                        audio("Ano atual:", todays_date.year) #colocar audio
                    if frase == "pupila em que mês estamos":  #colocar audio
                        audio("Mês atual:", todays_date.month) #colocar audio
                    if frase == "pupila que dia é hoje":  #colocar audio
                        audio("Dia atual:", todays_date.day)#colocar audio
                    #FIM
                    if frase == "Sair do pupila" or frase == "sair do pupila" :
                        audio("Adeus")
                        botao_x = 0
                        break   
                
            
        
            
            
            
        
            
        
            
        



        
        
        
        

        

        


        pygame.display.update()
 