#Seis Números Ímpares
a=int(input())
i=1
aux=a
while i<=6:
    if aux%2!=0:
        print(aux)
        i+=1
    aux+=1   