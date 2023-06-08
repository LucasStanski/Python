gols=[]
total_gols=0
jogo={"Nome":str(input("Qual é o nome do jogador: "))}
partidas=int(input(f"Quantas partidas {jogo['Nome']} Jogou: "))
for g in range(partidas):
    gols.append(int(input(f"Quantos gols na {g+1}° Partida: ")))
    total_gols+=gols[g]
    jogo["Gols"]=gols.copy()
    jogo["Total"]=total_gols
for k,v in jogo.items():
    print(f"O campo {k} tem o valor {v}.")
print(f"O jogador {jogo['Nome']} jogou {partidas} partidas.")
for k,v in enumerate(jogo["Gols"]):
    print(f" > Na partida {k+1}, {jogo['Nome']} fez {v} gols.")
print(f"No campeonato inteiro foi um total de {jogo['Total']} gols.")