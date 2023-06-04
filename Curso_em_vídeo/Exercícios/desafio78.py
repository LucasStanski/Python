valores=[]
contador=0
for cont in range(0,5):
    valores.append(int(input(f"Digite o {contador} valor: ")))
    contador+=1 
print(f"Os valores digitados foram {valores}")
print(f"O maior valor foi {max(valores)} na posiçao ",end="")
for i,v in enumerate(valores):
    if max(valores)==v:
        print(f"{i}",end="ª ")
print()
print(f"O menor valor foi {min(valores)} na posição ",end="")
for i,v in enumerate(valores):
    if min(valores)==v:
        print(f"{i}",end="ª ")
