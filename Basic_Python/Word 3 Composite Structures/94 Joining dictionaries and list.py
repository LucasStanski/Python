galera=[]
dados={}
soma=média=0
while True:
    dados.clear()
    dados["Nome"]=str(input("Digite o nome: "))
    while True:
        dados["Sexo"]=str(input("Qual é o seu sexo: ")).upper()[0]
        if dados["Sexo"] in "MF":
            break
        print("ERRO RESPONDA [M/F]")
    dados["Idade"]=int(input(f"Qual a sua idade: "))
    soma+=dados["Idade"]
    galera.append(dados.copy())
    resp=str(input("Quer continuar [S|N]: ")).upper()
    while resp not in "NS":
        resp=str(input("ERRO, QUER CONTINUAR S ou N: ")).upper()[0]
    if resp in "Nn":
        break
print()
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")
média=soma/len(galera)
print(f"A média de idade é de {média:5.2f} anos")
print("A mulheres cadastradas foram ",end="")
for p in galera:
    if p["Sexo"]=="F":
        print(f"{p['Nome']}, ",end="")
print()
print("Pessoas que estão com a idade acima da média: ")
for p in galera:
    if p['Idade']>=média:
        print("      ")
        for k,v in p.items():
            print(f"{k} = {v}; ",end="")