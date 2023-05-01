#Positivos e Média
num1=float(input())
num2=float(input())
num3=float(input())
num4=float(input())
num5=float(input())
num6=float(input())
i=0
media=0
if num1>0:
    i+=1
    media+=num1
if num2>0:
    i+=1
    media+=num2
if num3>0:
    i+=1
    media+=num3
if num4>0:
    i+=1
    media+=num4
if num5>0:
    i+=1
    media+=num5
if num6>0:
    i+=1
    media+=num6
media/=i
print("%d valores positivos" %i)
print("%.1f" %media)