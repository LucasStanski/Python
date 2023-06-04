numero=("Zero","um","Dois","Três","Quatro",
        "Cinco","Seis","Sete","Oito","Nove",
        "Dez","Onze","Doze","Treze","Quatorze",
        "Quinze","Dezesseis","Dezessete",
        "Dezoito","Dezenove","Vinte")
extenso=int(input("Digite um número de 0 a 20: "))
while extenso not in range(0,21):
    extenso=int(input("Tente novamente números de 0 a 20: "))
print(f"O número por extenso é {numero[extenso]}")