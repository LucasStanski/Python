print("        Cadastro de pessoas")
idade1 = homens = mulheres = 0
while True:
    idade=int(input("Idade: "))
    sexo=str(input("Sexo [M/F]: ")).upper().strip()
    quer=str(input("Quer continuar o cadastro [S/N]: ")).upper().strip()
    if quer=="N":
        break
    if idade>=18:
        idade1+=1
    if sexo=="M":
        homens+=1
    if sexo=="F" and idade<20:
        mulheres+=1
print(f"Existem {idade1} pessoas miores de 18 anos)")
print(f"Existem {homens} homens cadastrados")
print(f"Existem {mulheres} mulher com idade menor a 20 anos")
print("Acabou!!!")