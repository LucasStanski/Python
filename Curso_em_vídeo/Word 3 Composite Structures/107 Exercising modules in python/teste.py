import moeda1
p=float(input("Digite o preço R$: "))
print(f"A metade de {p} é R$ {moeda1.metade(p)} ")
print(f"O dobro de {p} é R$ {moeda1.dobro(p)}")
print(f"Aumentando 10%, temos R$ {moeda1.aumentar(p,10)}")
print(f"Diminuindo 13%, temos R$ {moeda1.diminuir(p,13)}")