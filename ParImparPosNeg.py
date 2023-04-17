#Pares, Ímpares, Positivos e Negativos
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
p=0
i=0
pos=0
neg=0
if num1%2==0:
    p+=1
else:
    i+=1 
if num2%2==0:
    p+=1
else:
    i+=1
if num3%2==0:
    p+=1
else:
    i+=1
if num4%2==0:
    p+=1
else:
    i+=1
if num5%2==0:
    p+=1
else:
    i+=1

if num1>0 and num1!=0:
    pos+=1
elif num1<0:
    neg+=1
if num2>0 and num2!=0:
    pos+=1
elif num2<0:
    neg+=1
if num3>0 and num3!=0:
    pos+=1
elif num3<0:
    neg+=1
if num4>0 and num4!=0:
    pos+=1
elif num4<0:
    neg+=1
if num5>0 and num5!=0:
    pos+=1
elif num5<0:
    neg+=1

print("%d valor(es) par(es)" %p)
print("%d valor(es) impar(es)" %i)
print("%d valor(es) positivo(s)" %pos)
print("%d valor(es) negativo(s)" %neg)