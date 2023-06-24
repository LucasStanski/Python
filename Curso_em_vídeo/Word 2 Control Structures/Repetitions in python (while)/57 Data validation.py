#M="M"or"F"
#
#while M == "M"or"F":
#    sexo=str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
#   if sexo==M:
#        print("Ok, já está arquivado")
#    if sexo!=M:
#        print("Degite o valor correspondente")

sexo=str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo=str(input("Digite certo M ou F: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso!!! ")