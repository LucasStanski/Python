print("     Lista de produtos")
total= mais = menor= cont=0
barato=""
while True:
    preço=float(input("Digite o preço do produto R$: "))
    nome=str(input("Digite o nome do produto: ")).upper().strip()
    quer=str(input("Quer continuar [S/N]: ")).upper().strip()[0]
    if quer=="N":
        print("Saindo...")
        break
    total+=preço
    if preço>1000.00:
        mais+=1
    if cont==1 or preço<menor:
        menor=preço
        barato=nome
print("Fim")
print(f"O total da compra foi {total}")
print(f"Temos um total de {mais} custando mil reais")
print(f"O produto mais barato foi {barato}")