vetor  = []
i= 0
def substituir_numero(vetor):
    i= 0
    while i<=5:
        x=vetor[i]
        if x<10 and x>=0:
            vetor[i]=1
        elif x<0:
            vetor[i]=0
        else:
           vetor[i]=2
        i = i+1
    print(vetor)
while i<=5:
    j = int(input("Digite um numero:  "))
    vetor.append(j)
    i=i+1
substituir_numero(vetor)
    
    
    
    
