from time import sleep
continuar=False
valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
while not continuar:
    sleep(1)
    print("-"*14)
    print("MENU DE OPÇÕES")
    print("-"*14)
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair do programa")
    valor3=int(input("Oque você quer fazer com os números? "))
    if valor3==1:
        resultado1=valor1+valor2
        print(f"A soma de {valor1} + {valor2} = {resultado1}")
    elif valor3==2:
        resultado2=valor1*valor2
        print(f"A multiplicação entre {valor1} x {valor2} = {resultado2}")
    elif valor3==3:
        if valor1>valor2:
            print(f"{valor1} é maior que {valor2}")
        elif valor2>valor1:
            print(f"{valor2} é maior que {valor1}")
        else:
            print("Os dois valores são iguais")
    elif valor3==4:
        print("Informe os números novamente")
        valor1=int(input("Primeiro Valor: "))
        valor2=int(input("Segundo valor: "))
    elif valor3==5:
        print("Finalizando.....")
        exit(continuar)
    else:
        print("Opçao inválida, tente novamente...")