#O Maior
valor = input().split(" ")
a, b, c = valor
a=int(a)
b=int(b)
c=int(c)
maiorab=(a+b+abs(a-b))/2
maior=(maiorab+c+abs(maiorab-c))/2
print("%d eh o maior" %maior)