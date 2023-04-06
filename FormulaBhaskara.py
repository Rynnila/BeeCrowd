valores=input().split(" ")
a,b,c = valores

a=float(a)
b=float(b)
c=float(c)

delta=b**2-(4*a*c)


if delta<=0:
    print("Impossivel calcular")
else:
    r1= ((-b)+delta**(1/2))/2*a
    r2= ((-b)-delta**(1/2))/2*a
    print("R1 = %.5f\nR2 = %.5f" %(r1,r2))