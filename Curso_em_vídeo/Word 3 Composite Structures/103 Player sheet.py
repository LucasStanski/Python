def ficha(Jog="<desconhecido>",gols=0):
    print(f"O Jogador {Jog} fez {gols} gol(s) no campeonato.")


n=str(input("Nome do jogador: "))
g=str(input("Número de gols: "))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=="":
    ficha(gols=g)
else:
    ficha(n,g) 