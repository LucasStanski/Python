import random
n1=int(input("Digite um número de 0 a 5: "))
random=random.randint(0,5)
if n1==random:
    print("Você acertou")
else:
    print("Você errou")

