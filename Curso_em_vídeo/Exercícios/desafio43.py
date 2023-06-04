print("*"*15)
print("Calculo IMC")
print("*"*15)
peso=float(input("Qual seu peso? "))
altura=float(input("Qual a sua altura? "))
IMC=peso/(altura*altura)
print(f"Seu IMC é {IMC:.2f}")
if IMC<=18.5:
    print("Abaixo do peso")
elif IMC>18.5 and IMC<25:
    print("Peso ideal")
elif IMC>25 and IMC<30:
    print("Sobrepeso")
elif IMC>30 and IMC<40:
    print("Obesidade")
else:
    print("Obesidade Mórbida MORTEEE")
