pessoas=[]
dado=[]
maior=menor=0
while True:
    pessoas.append(str(input("Digite o nome: ")))
    pessoas.append(float(input("Digite o peso: ")))
    if len(dado)==0:
        maior=menor=pessoas[1]
    else:
        if pessoas[1]>maior:
            maior=pessoas[1]
        if pessoas[1]<menor:
            menor=pessoas[1]
    dado.append(pessoas[:])
    pessoas.clear()
    resp=str(input("Quer continuar [S|N]: ")).upper()
    while resp not in "NS":
        resp=str(input("QUER CONTINUAR S ou N: ")).upper()
    if resp in "Nn":
        break
print("As pessoas cadastradas foram: ")
print(f"Você cadastrou {len(dado)} pessoas ")
print(f"O maior peso foi de {maior}kg. Peso de ",end="")
for p in dado:
    if p[1]==maior:
        print(f"[{p[0]}] ",end="")
print()
print(f"O menor peso foi de {menor}kg. Peso de ",end="")
for p in dado:
    if p[1]==menor:
        print(f"[{p[0]}] ",end="")
print()
