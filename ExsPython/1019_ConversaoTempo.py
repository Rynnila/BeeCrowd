#Conversâo Tempo
n=int(input())
horas=n//3600
n=n-horas*3600
minutos=n//60
n=n-minutos*60
print("%d:%d:%d" %(horas,minutos,n))