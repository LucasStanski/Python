somaidade=0
médiaidade=0
maioridadedehomem=0
nomevelho=""
totmulher20=0
for p in range(1,5):
    print(f"----{p}°PESSOA----")
    nome=str(input("Qual é seu nome: ")).strip()
    idade=int(input(f"Sua idade {nome}: "))
    sexo=str(input("Qual é seu sexo [M/F]: ")).strip()
    somaidade+=idade
    if p==1 and sexo in "Mm":
        maioridadedehomem=idade
        nomevelho=nome
    if sexo in "Mm" and idade>maioridadedehomem:
        maioridadedehomem=idade
        nomevelho=nome
    if sexo in "Ff" and idade<20:
        totmulher20+=1
médiaidade=somaidade/4
print(f"A média de idade é {médiaidade}")
print(f"O homem mais velho tem {maioridadedehomem} e se chama {nomevelho}")
print(f"Ao todo são {totmulher20} com menos de 20 anos")