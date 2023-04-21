#Sorteio Simples
a, b, c= map(int, input().split())
if a<b and a<c:
    menor=a
    if b<c:
        print("%s\n%s\n%s\n" %(menor, b, c))
    else:
        print("%s\n%s\n%s\n" %(menor, c, b))
elif b<a and b<c:
    menor=b
    if a<c:
        print("%s\n%s\n%s\n" %(menor, a,c))
    else:
        print("%s\n%s\n%s\n" %(menor, c,a))
elif c<a and c<b:
    menor=c
    if a<b:
        print("%s\n%s\n%s\n" %(menor, a,b))
    else:
        print("%s\n%s\n%s\n" %(menor, b, a))
print("%s\n%s\n%s" %(a,b,c))
