#Aumento de salário
sal=float(input())
if sal>0 and sal<=400:
    r=sal*0.15
    sal=sal+r
    p="15"
elif sal>400 and sal<=800:
    r=sal*0.12
    sal=r
    p=12
elif sal>800 and sal<=1200:
    r=sal*0.10
    sal=sal+r
    p=10
elif sal>1200 and sal<=2000:
    r=sal*0.07
    sal=sal+r
    p=7
elif sal>2000:
    r=sal*0.04
    sal=sal+r
    p=4
print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %s %%" %(sal, r, p))