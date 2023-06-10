from random import randint
from time import sleep


def sorteio(lista):
    print("Sorteando 5 valores da lista: ",end="")
    for p in range(0,5):
        aleatorio=randint(1,10)
        lista.append(aleatorio)
        print(f"{aleatorio} ",end="", flush=True)
        sleep(0.3)
    print("PRONTO")


def somaPar(lista):
    somapar1=0
    for n in lista:
        if n%2==0:
            somapar1+=n
    print(f"Somando os valores pares de {lista}, temos {somapar1}")
          
            
números=list()
sorteio(números)
somaPar(números)