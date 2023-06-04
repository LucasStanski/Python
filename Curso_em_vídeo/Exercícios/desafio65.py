#from time import sleep
#continuar=False
#soma=0
#quantidade=0
#while not continuar:
#    print("-"*20)
#    num=int(input("* Digite um número: "))
#    soma=soma+num
#    média=soma/quantidade
#    print("[1] SIM [2] NÃO")
#    quer=int(input("Quer continuar: "))
#    if quer==1:
#        quantidade+=1
#        continue
#    elif quer==2:
#        print("Finalizando...")
#        print(soma)
#        break

x=str(input("Quer brincar de somar números? [S/N]: ")).upper().strip()
contador=0
while x=="S":
    num=int(input("Digite um número: "))
    contador+=num
    x=str(input("Quer continuar somando? [S/N]: ")).upper().strip()
print(f"A soma total foi de {contador}")