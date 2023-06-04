km = float(input('Quantos kms foram percorridos? '))
d = int(input('Por quantos dias o carro foi alugado? '))
total = (km * 0.50) + (d * 60) 
print(f"O valor total a ser pago é de: R${total:.2f}")