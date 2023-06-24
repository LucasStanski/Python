import random
pc=random.randint(0,10)
palpites=0
acertou=False
while not acertou:
    jogador=int(input("De um palpite para acertar: "))
    if jogador==pc:
        print("Você acertou")
        palpites+=1
        break
    else:
        print("Você errou")
        palpites+=1
print(f"Você acertou com {palpites} palpites")