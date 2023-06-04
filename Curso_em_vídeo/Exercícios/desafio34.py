salário=int(input("Quantos você ganha? "))
if salário>=1250:
    novo=salário+(salário*15/100)
    print(f"Você agora ganha {novo} com um aumento de 10%")
elif salário<=1250:
    novo1=salário+(salário*15/100)
    print(f"Seu salário agora é de {novo1} com um aumento de 15%")