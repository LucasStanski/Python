ano=int(input("Qual seu ano de nascimento atleta? "))
if ano<=9:
    print("Você se encontra na categoria mirim")
elif ano<=14:
    print("Você se encontra na categoria infantil")
elif ano<=19:
    print("Você se encontra na categoria junior")
elif ano<=20:
    print("Você se encontra na categoria senior")
else:
    print("Você se encontra na categoria master")