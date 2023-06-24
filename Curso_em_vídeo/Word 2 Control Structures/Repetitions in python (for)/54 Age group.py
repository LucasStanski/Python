from datetime import date
#ano_atual=date.today().year
#s=0
#for i in range(0, 7):
#   ano = int(input("Digite o ano de nascimento: "))
#    s=ano_atual-ano
#    if s<=2005:
#        print(f"Você já é de maior")
#   if s>=2005:
#        print(f"Você ainda é de menor")
atual=date.today().year
totmaior=0
totmenor=0
for pess in range(1,8):
    nas=int(input(f"Em que ano a {pess} pessoa nasceu? "))
    idade=atual-nas
    if idade>=21:
        totmaior+=1
    else:
        totmenor+=1
print(f"Ao todo tivemos {totmaior} pessoas maiores de idade e {totmenor} menores")