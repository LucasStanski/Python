valor_casa=int(input("Quantos você quer pagar na casa? "))
salario=int(input("Quantos você ganha de salário? "))
anos_pagar=int(input("Em quantos anos você vai pagar? "))
prestacoo= valor_casa/(anos_pagar*12)
minimo=salario*30/100
print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos_pagar} anos, a prestação será {prestação:.2f}")
if prestação<=minimo:
    print("Emprestimo CONCEDIDO")
else:
    print("Emprestimo NEGADO")
