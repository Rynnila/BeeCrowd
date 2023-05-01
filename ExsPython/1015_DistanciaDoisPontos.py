#Distância entre dois pontos
p1=input().split(" ")
p2=input().split(" ")

x1, y1=p1
x2, y2=p2

x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)

distancia=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
print("%.4f" %distancia)