cont = soma = 0
print("Digite 999 para parar")
continuar=False
while not continuar:
    num=int(input("Digite um número: "))
    cont+=1
    soma=soma+num
    soma1=soma-999
    if num==999:
        print("Finalizando...")
        break
print(f"Você digitou {cont-1} números, e a soma entre eles foi {soma1}")
    
#núm=cont=soma=0
#núm=int(input("Digite um número [999 para parar]: "))
#while núm!=999:
#    soma+=núm
#    cont+=1
#    núm=int(input("Digite um número [999 para parar]: "))
#print(f"Você digitou {cont} números e a soma entre eles foi {soma}")