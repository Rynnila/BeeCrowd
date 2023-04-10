#Lanche
cod, quant = input().split(" ")

cod=int(cod)
quant=int(quant)
if cod==1:
    total=float(quant*4.00)
elif cod==2:
    total=float(quant*4.50)
elif cod==3:
    total=float(quant*5.00)
elif cod==4:
    total=float(quant*2.00)
elif cod==5:
    total= float(quant*1.50)
print("Total: R$ %.2f" %total)