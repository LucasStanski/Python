print("***************************")
print("         Triângulo         ")
print("***************************")
r1=float(input("Digite o primeiro lado: "))
r2=float(input("Digite o segundo lado: "))
r3=float(input("Digite o terceiro lado: "))
if r1< r2+r3 and r2< r1+r3 and r3< r1+r2:
    if r1==r2==r3:
        print("O tiângulo é Equilatero")
    elif r1==r2 or r2==r3 or r1==r3:
        print("O triângulo é Isósceles")
    else:
        print("O triângulo é Escaleno")
    print("Pode ser formada um triângulo")
else: 
    print("Não pode ser formado ;-; ")
