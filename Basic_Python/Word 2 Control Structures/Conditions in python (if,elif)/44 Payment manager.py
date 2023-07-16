preço=int(input("Qual o preço do produto: "))
print("Método de pagamento: ")
print("[1] Dinheiro [2] cartão")
print("[3] 2x no cartão [4] 3x ou mais no cartão")
método_pag=int(input("Qual método? "))
if método_pag==1:
    vista=preço-(preço*10/100)
    print(f"Você irá pagar {vista} com desconto de 10% ao pagar á vista e em dinheiro")
elif método_pag==2:
    vista1=preço-(preço*5/100)
    print(f"Você irá pagar {vista1} com desconto de 5% ao pagar á vista no cartão")
elif método_pag==3:
    print(f"Você irá pagar {preço} porque parcelou em 2x no cartão")
else:
    n_parcelas=int(input("Em quantas parcelas você irá pagar? "))
    vista3=preço+(preço*20/100)
    n_parcelas1=vista3//n_parcelas
    print(f"Você irá pagar no total {vista3} com cada parcela valendo {n_parcelas1} com juros de 20%")