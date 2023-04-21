#Triângulp
A,B,C = map(float,input().split())
if (A+B)>C and (A+C)>B and (B+C)>A:
    perimetro = (A+B+C)
    print("Perimetro = %.1f" %perimetro)
else:
    area = 0.5*(A+B)*C
    print("Area = %.1f" %area)