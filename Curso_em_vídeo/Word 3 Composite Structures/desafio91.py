from random import randint
from time import sleep
from operator import itemgetter
jogadores={'jogador-1':randint(1,6),'jogador-2':randint(1,6),'jogador-3':randint(1,6),'jogador-4':randint(1,6),}
print()
for k,v in jogadores.items():
    print(f"{k} jogou o dado, e caiu no número {v}")
    sleep(1)
print("="*25)
print("   Rank dos Jogadores")
print("="*25)
rank=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(rank):
    print(f"{i+1}° Lugar: {v[0]} com {v[1]}")
    sleep(1)
print()