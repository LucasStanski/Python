import random
letra_maiuscula= chr(random.randint(65,90))
letra_minuscula=chr(random.randint(97,122))
caractere=chr(38)
numeros=[]
for i in range(12):
    numeros1=random.randrange(9)
    numeros.append(numeros1)

random.shuffle(numeros)
numeros=str(numeros)[1:-1]
numeros=numeros.replace(",","")
print(letra_minuscula,letra_maiuscula,numeros,caractere)