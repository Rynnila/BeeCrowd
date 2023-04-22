#Tempo de Jogo
i, f = input().split()

i = int(i)
f = int(f)

if i < f:
    t = f - i
else:
    t = (24 - i) + f
print('O JOGO DUROU %d HORA(S)'%t)