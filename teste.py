from datetime import date
data_atual = date.today()
data_em_texto = data_atual.strftime("%d/%m/%Y")


def fala_data (x): #retorn a data toda junta
    retorna = ""
    for i in x:
        if i != "/":
            retorna = retorna + i
    return retorna
    
j = fala_data (data_em_texto)
print ("A data atual é" + fala_data(data_em_texto[0:2]))
print ("A data atual é" + fala_data(data_em_texto[3:5]))
print ("A data atual é" + fala_data(data_em_texto[6:10]))

    
    