listagem=("Pão", 7.35,
          "Arroz", 20.00,
          "Feijão", 8.00,
          "Mandioca", 5.00,
          "Batata", 3.00,
          "Farofa", 6.99,
          "Macarrão", 4.59)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}",end="")
    else:
        print(f"R${listagem[pos]:>7.2f}")