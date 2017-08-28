#Criando um objeto do tipo file
temp = open("primeiro.txt", "w")

#Escrevendo no arquivo
texto = "PALMEIRAS NÃO TEM MUNDIAL!!!"
temp.write(texto)

#fechando arquivo
temp.close()
