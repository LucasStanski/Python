valor=[]
par=[]
impar=[]
while True:
    num=int(input("Digite um número: "))
    valor.append(num)
    if num%2==0:
        par.append(num)
    else:
        impar.append(num)
    resp=str(input("Quer continuar [S|N]: ")).upper()
    while resp not in "NS":
        resp=str(input("QUER CONTINUAR S ou N: ")).upper()
    if resp in "Nn":
        break
print(f"A lista com todos os valores é: {valor}")
print(f"A lista com os valores par é: {par}")
print(f"A lista com os valores impares é: {impar}")