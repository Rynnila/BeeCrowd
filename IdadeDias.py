#Idade em dias
idade=int(input())
anos=idade//365
idade-=anos*365
meses=idade//30
idade-=meses*30
dias=idade
print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(anos,meses, dias))