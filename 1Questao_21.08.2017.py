vetor = []
i = 0
while i <=5:
    j = int(input("digite  um numero: "))
    if j>0:
        vetor.insert(i,1)
    else:
        vetor.insert(i,0)
    i = i+1
print (vetor)
