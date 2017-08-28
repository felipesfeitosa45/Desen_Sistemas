
def copiarArquivo(primeiro, segundo):
    p1 = open("primeiro.txt", "r")
    p2 = open("segundo.txt", "w")

    for texto in p1:
        p2.write(texto)
    p1.close()
    p2.close()

copiarArquivo("primeiro.txt","segundo.txt")        

