viagem=int(input("Quantos km é o seu destino: "))
if viagem<=200:
    valor1=viagem*0.50
    print(f"Você irá pagar {valor1} na sua passagem")
else:
    valor2=viagem*0.45
    print(f"Você irá pagar {valor2} na sua passagem")