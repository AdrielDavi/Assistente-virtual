from datetime import date 
import speech_recognition as sr
import cv2
import pytesseract
import pyscreenshot 
import os
import pyttsx3 #tem função de ler txt e pdf
#bbox=(10,10,500,500) -- corta a tela do print
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
        print("sim")
        os.startfile("https://www.youtube.com/watch?v=pWjmpSD-ph0")
    #DATA
    if frase == "pupila qual a data de hoje":  #colocar audio
        print("Data atual: ", todays_date)           #colocar audio
    if frase == "pupila em que ano estamos":  #colocar audio
        print("Ano atual:", todays_date.year) #colocar audio
    if frase == "pupila em que mês estamos":  #colocar audio
        print("Mês atual:", todays_date.month) #colocar audio
    if frase == "pupila que dia é hoje":  #colocar audio
        print("Dia atual:", todays_date.day)#colocar audio
    

    #FIM
    if frase == "Sair do pupila" or frase == "sair do pupila" :
        print("Adeus")
        break
         



















#imagem = pyscreenshot.grab() #tira o print
#imagem.save("tela.png") # Salva com o nome tela
#img = cv2.imread("tela.png") #ler a imagem
#pytesseract.pytesseract.tesseract_cmd = ("C:\Program Files\Tesseract-OCR\Tesseract.exe") #caminho
#resultado = pytesseract.image_to_string(img) #Converte a imagem para string
#print (resultado)

