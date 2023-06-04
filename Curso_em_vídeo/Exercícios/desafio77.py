palavras=("Sabedoria","Saber","Viver","Astronauta","Caxumba","Trator",
          "Corredor","Programador","Escavadeira","Professor",
          "Diamante","Ouro","Safira","Rubi","Cristal")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos: ",end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra,end=" ")