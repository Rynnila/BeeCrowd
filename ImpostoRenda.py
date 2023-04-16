#Imposto de Renda
sal = float(input())

if(sal > 0 and sal <= 2000):
 print("Isento")
elif(sal > 2000 and sal <= 3000):
 resto = sal - 2000
 resultado = resto * 0.08
 print("R$ %.2f" %resultado)
elif(sal > 3000 and sal < 4500):
 resto = sal - 3000
 resultado = (resto * 0.18) + (1000 * 0.08)
 print("R$ %.2f" %resultado)
else:
 resto = sal - 4500
 resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
 print("R$ %.2f" %resultado)