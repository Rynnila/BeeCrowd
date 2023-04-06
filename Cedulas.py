#Cédulas
n=int(input())
print(n)
nota100=n//100
n=n-nota100*100

nota50=n//50
n=n-nota50*50

nota20=n//20
n=n-nota20*20

nota10=n//10
n=n-nota10*10

nota5=n//5
n=n-nota5*5

nota2=n//2
n=n-nota2*2

nota1=n//1
n=n-nota1

print("%d nota(s) de R$100,00 " %nota100)
print("%d nota(s) de R$50,00 " %nota50)
print("%d nota(s) de R$20,00 " %nota20)
print("%d nota(s) de R$10,00 " %nota10)
print("%d nota(s) de R$5,00 " %nota5)
print("%d nota(s) de R$2,00 " %nota2)
print("%d nota(s) de R$1,00" %nota1)