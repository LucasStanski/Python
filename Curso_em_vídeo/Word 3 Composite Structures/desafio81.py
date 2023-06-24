lista=[]
while True:
    num=int(input("Digite um número: "))
    lista.append(num)
    resp=str(input("Quer continuar [S|N]: ")).upper()
    while resp not in "NS":
        resp=str(input("QUER CONTINUAR S ou N: ")).upper()
    if resp in "Nn":
        break
print()
quantidade=len(lista)
lista.sort(reverse=True)
if 5 in lista:
    print("A lista possui o valor 5")
    #resp1=str(input("Quer saber a posição do primeiro valor 5 ? [S/N]: #")).upper()
    #print("="*40)
    #while resp1 not in "NS":
    #    resp1=str(input("QUER CONTINUAR S ou N: ")).upper()
    #    if resp1 in "Nn":
    #        break
    #print(f"O primeiro valor cinco citado na lista está na posção:",#lista.index(5)+1)
else:
    print("A lista não possui o valor 5")
print(f"Foram digitados {quantidade} números no total")
print(f"A lista com os número decrecentes fica assim {lista}")
print()

