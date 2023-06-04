maior=0
menor=0
for p in range(1,6):
    peso=float(input(f"Digite o peso da {p}° pessoa: "))
    if p == 1:
        maior=p
        menor=p
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print(f"O maior peso foi de {maior} kilos")
print(f"O menor peso foi de {menor} Kilos")