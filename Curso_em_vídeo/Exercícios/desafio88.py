from random import randint
lista=[]
contador=0
while True:
    num=randint(1,60)
    if num in lista:
        lista.append(num)
        contador+=1
    if contador >=6:
        break
print(f"Os números soteados foram {lista}")
