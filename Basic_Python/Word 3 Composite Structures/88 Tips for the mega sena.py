from random import randint
lista=[]
jogos=[]
quantidade=int(input("Quantos jogos você quer que eu sorteie? "))
total=1
while total<=quantidade: 
    contador=0
    while True:
        num=randint(1,60)
        if num in lista:
            lista.append(num)
            contador+=1
        if contador >=6:
            break
    lista.sort()
    jogos.append(lista)
    lista.clear()
    total+=1
print("-="*30, f"sorteando {quantidade} jogos", "-="*30)
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    

