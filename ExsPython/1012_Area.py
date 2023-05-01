#area
valor = input().split(" ")

a, b, c = valor
a=float(a)
b=float(b)
c=float(c)
triangulo=(a*c)/2
circulo=3.14159*c**2
trapezio=((a+b)*c)/2
quadrado=b**2
retangulo=a*b
print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" %(triangulo, circulo, trapezio, quadrado, retangulo))
