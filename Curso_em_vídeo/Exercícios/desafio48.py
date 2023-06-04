#par = 0
#for c in range(0, 501):
#    if c % 3 == 0:
#        if c % 2 == 1:
#            par += c
#            print(f"{c} Número Impar multiplo de 3")
#print(f"A soma dos numeros impares multiplos de 3 resulta {par}")

#acomuladores
soma=0
cont=0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont=cont+1
        soma=soma+c
print(f"A soma é {soma}")
print(f"Foram {cont} números solicitados")