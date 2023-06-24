valores=[[],[]]
contador=1
for cont in range(0,5):
    valor=int(input(f"Digite o {contador} valor: "))
    contador+=1
    if valor%2==0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f"Os valores foram: {valores}")
print(f"Os valores pares foram: {valores[0]}")
print(f"Os valores impares foram: {valores[1]}")