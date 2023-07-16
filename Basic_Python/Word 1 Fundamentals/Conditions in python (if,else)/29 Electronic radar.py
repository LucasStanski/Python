multa=80
velo_car=int(input("Digite a velocidade do carro: "))
if velo_car >= 80:
    valor=velo_car-80
    print(f"Você levou uma multa de exesso de velocidade no valor de {valor*7} reais")
else:
    print("Você está no limite da via")