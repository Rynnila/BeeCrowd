#Intervalo2
n = int(input())
dentro = 0
fora = 0
for i in range(1,n + 1):
    x = int(input())
    if x >= 10 and x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print('%d in'%dentro)
print('%d out'%fora)