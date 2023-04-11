A,B,C,D=map(float,input().split())

media= (A*2+B*3+C*4+D*1)/10
print("Media: %.1f" %media)
if media>=7:
    print("Aluno aprovado.")
elif media<5:
    print("Aluno reprovado.")
elif media<=6.9 and media>=5:
    print("Aluno em exame.")
    exame=float(input())
    print("Nota do exame: %.1f" %exame)
    media=(media+exame)/2
    if media>=5:
        print("Aluno aprovado.")
        print("Media final: %.1f" %media)
    elif media<=4.9:
        print("Aluno reprovado.")
        print("Media final: %.1f" %media)