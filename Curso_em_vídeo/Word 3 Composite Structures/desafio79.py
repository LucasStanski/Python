lista=[]
while True:
    valores=int(input(f"Digite o valor: "))
    if valores in lista:
        print("Esse valor contem na lista")
    else:
        lista.append(valores)
    resp=str(input("Quer continuar [S|N]: ")).upper()
    while resp not in "NS":
        resp=str(input("QUER CONTINUAR Sim ou Não: ")).upper()
    if resp in "N":
        break
lista.sort()
print(f'Os números digitados foram {lista}.')


