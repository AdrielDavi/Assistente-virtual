# Teste 1

# Para testar se o código reconhece corretamente a frase "Olá mundo" dita no microfone, podemos usar o seguinte código para retornar apenas a frase "Olá mundo" quando ela é reconhecida. 
# Em seguida, podemos escrever um teste utilizando a biblioteca pytest que verifica se a frase retornada pela função é exatamente "Olá mundo".

import speech recognition as sh

def ouvir microfone():
    microfone = sr.Recognizer() 
    with sr.Microphone() as source:
        microfone.adjust_for_ambient noise(source)
        print("Diga alguma coisa: ") 
        audio microfone.listen(source)
    try:
        frase microfone.recognize_google (audio, language="pt-BR") 
        print("voce disse: " + frase)
        if frase.lower() == "Olá mundo":
            return "Olá mundo"
        else:
            return "Frase diferente de 'Olá mundo'"
    except sr.UnknownValueError: 
        print("Não entendi")
        return "Não entendi"

def test_ouvir microfone(): 
    assert ouvir microfone() == "Olá mundo"
    
# Execute o pytest e diga 'Olá mundo'

# Teste 2

# Esse teste usa a função input para pedir ao usuário para confirmar se o texto foi lido corretamente em voz alta ou não.
# Depois de executar o teste, o resultado será exibido no terminal. Se o teste passar, a mensagem "1 passed in ..." será exibida. Se o teste falhar, uma mensagem de erro será exibida indicando a causa do erro.

import pyttsx

def audio(text):
    speaker = pyttsx3.init() 
    speaker.say(texto)
    speaker.runAndwait()

def test_audio():
    texto "Este é umteste de áudio."
    audio(texto)
    # Verifica se o texto é falado corretamente em voz alta
    assert input(f"O texto a seguir foi lido corretamente em voz alta ? '{texto}' (sim ou não): ").lower() == "sim"

# Quando digitado "sim"
# Saída: O texto a seguir foi lido corretamente em voz alta ? 'Este é um teste de áudio.' (sim ou não): sim
# Quando digitado "não"
# Saída: FAILURE test_sample.py::test_audio - AssertionError: assert 'não' == 'sim'

# Teste 3

# Nesse teste, a função "abrir_google" é chamada com uma frase de entrada correta e a lista de processos em execução é obtida antes e depois da abertura do Chrome.
# Em seguida, é percorrida a lista de processos depois da abertura do Chrome em busca do processo do Chrome, verificando se o processo não estava presente na lista de processos antes da abertura.
# Se o processo do Chrome estiver presente na lista de processos após a abertura, a variável "chrome_aberto" é definida como True. Biblioteca "psutil" para listar os processos em execução antes e depois de abrir o Google Chrome e verificar se o processo do Chrome está  presente na lista de processos após a abertura.
# Por fim, o teste verifica se a variável "chrome_aberto" é True, indicando que o Chrome foi aberto corretamente. Se o teste passar, a mensagem "1 passed in ..." será exibida. Se o teste falhar, uma mensagem de erro será exibida indicando a causa do erro.

import os
import pyttsx3
import psutil

speaker pyttsx3.init()

def abrir_google(frase):
    if frase == "pupila abrir google" or frase == "pupila abrir o google" or frase == "pupila abra o google" 
    speaker.say("abrindo o google") #define o texto que será lido
    speaker.runAndWait()
    os.system("start chrome")

def test_abrir_google():
    frase_correta = "pupila abrir o google"
    abrir_google(frase_correta)
    # Verifica se o chrome é aberto
    chrome_aberto = False
    for proc in psutil.process_iter(['name']): 
        if proc.info['name'] == 'chrome.exe':
            chrome_aberto - True
            break
    assert chrome_aberto == True
    
# Saída: 1 passed in alguns segundos...

# Teste 4
# A nova funcionalidade incorporada possibilita a realização de cálculos de valores fornecidos pelo usuário por meio do microfone.
# A string convertida é posteriormente processada pela função eval do Python, a qual retorna o resultado da expressão avaliada.

import speech_recognition as sr
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()
    # usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    try:
        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')
        # Retorna a frase pronunciada
        print("Você disse: " + frase)
        return frase
    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")
    return ""
def calcular(expressao):
    try:
        resultado = eval(expressao)
        return resultado
    except Exception as e:
        return str(e)
def test_calculo():
    frase = "quanto é 2 + 2"
    resultado_esperado = 4
    assert calcular(frase[8:]) == resultado_esperado
    frase = "quanto é 10 * 5"
    resultado_esperado = 50
    assert calcular(frase[8:]) == resultado_esperado
    frase = "quanto é 10 / 0"
    resultado_esperado = "division by zero"
    assert calcular(frase[8:]) == resultado_esperado
if __name__ == "__main__":
    frase = ouvir_microfone()
    if frase.startswith("quanto é"):
        resultado = calcular(frase[8:])
        print(resultado)

# O pytest encontrará automaticamente a função de teste test_calculo e a executará. Ele informará se os testes passaram ou falharam..
# A mensagem "test session starts" indica que a sessão de testes está começando. Em seguida, são exibidas informações sobre a plataforma em que os testes estão sendo executados, incluindo a versão do Python (3.10.7), a versão do pytest (7.3.1) e a versão do pluggy (1.0.0). Essas informações podem ser úteis para diagnóstico ou solução de problemas relacionados às versões dos componentes envolvidos.
# A linha "rootdir: C:\Users\adrie\Desktop\sei lá" mostra o diretório raiz em que o pytest está sendo executado. Nesse caso, o pytest está sendo executado a partir do diretório "sei lá" no caminho "C:\Users\adrie\Desktop\".
# A próxima linha "collected 1 item" informa que o pytest coletou um arquivo de teste para ser executado.
# Em seguida, é exibido o nome do arquivo de teste (1_test.py) e um ponto final "." indicando que o teste passou com sucesso. Se houvesse falhas ou erros nos testes, seriam exibidos outros caracteres ou informações adicionais indicando as falhas específicas.
# Por fim, a última linha "1 passed in 0.27s" indica que 1 teste passou com sucesso em 0.27 segundos.
# Essa é uma mensagem típica de execução bem-sucedida do pytest. Ela indica que o teste foi concluído sem erros ou falhas.

