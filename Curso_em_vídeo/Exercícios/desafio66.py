import random

import randint
cont = soma = 0
a=random.randint
while True:
    num=int(input("Digite um número [999 para parar]    : "))
    if num==999:
        break
    soma+=num
    cont += 1
print(f"Foram {cont} números escritos e a soma entre eles é {soma}")
print("Acabou")