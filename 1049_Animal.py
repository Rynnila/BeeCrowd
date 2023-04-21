#Animal
pal1=input()
pal2=input()
pal3=input()

if pal1=="vertebrado":
    if pal2=="ave":
        if pal3=="carnivoro":
            print("aguia")
        elif pal3=="onivoro":
            print("pomba")
    elif pal2=="mamifero":
        if pal3=="onivoro":
            print("homem")
        if pal3=="herbivoro":
            print("vaca")
if pal1=="invertebrado":
    if pal2=="inseto":
        if pal3=="hematofago":
            print("pulga")
        elif pal3=="herbivoro":
            print("lagarta")
    elif pal2=="anelideo":
        if pal3=="hematofago":
            print("sanguessuga")
        if pal3=="onivoro":
            print("minhoca")