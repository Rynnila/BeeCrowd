#Tipos de triângulo 
A,B,C=list(map(float,input().split()))
if(A < B):
    X = A
    A = B
    B = X
if(B < C):
    X = B
    B = C
    C = X
if(A < B):
    X = A
    A = B
    B = X

if(A>=(B+C)):
    print("NAO FORMA TRIANGULO")
elif(A*A == (B*B+C*C)):
     print("TRIANGULO RETANGULO")
elif(A * A > (B*B+ C*C)):
    print("TRIANGULO OBTUSANGULO")
elif(A*A<(B*B + C*C)):
    print("TRIANGULO ACUTANGULO")
if(A == B and B == C):
        print("TRIANGULO EQUILATERO")
elif(A == B or B == C):
        print("TRIANGULO ISOSCELES")
