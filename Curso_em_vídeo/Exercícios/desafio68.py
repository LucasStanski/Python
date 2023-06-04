#import random
#vitórias=0
#while True:
#    computador = random.randint(1, 5)
#    escolha=int(input("Oque você irá escolher jogador? [1] Par [2] Impar: "))
#    numero=int(input("E qual o número você irá escolher [1 até 5]: "))
#    soma=computador+numero
#    print(f"J={numero} M={computador} Total={soma}")
#    if escolha==1:
#        if soma%2==0:
#            vitórias+=1
#            print("Jogador ganhou")
#        else:
#            print("Maquina ganhou")
#            break
#    if escolha == 2:
#        if soma%2==1:
#            print("Jogador ganhou")
#            vitórias += 1
#        else:
#            print("Maquina ganhou")
#            break
#print(f"O jogador conseguiu um total de {vitórias} vitória contra máquina.")
#print("Acabou")

from random import randint
v=0
while True:
    jogador=int(input("Informe um valor: "))
    computador=randint(0,10)
    total=jogador+computador
    tipo=""
    while tipo not in "PI"
        tipo=str(input("Oque você irá escolher P ou I: "))
    print(f"Você jogou {jogador} e o computador {computador} total de {total}")
    if tipo=="P":
        if total%2==0:
            print("você venceu!")
            v+=1
        else:
            print("Você perdeu!")
            break
    elif tipo=="I":
        if total%2==1:
            print("Você ganhou!")
            v+=1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"Você venceu {v} vezes")