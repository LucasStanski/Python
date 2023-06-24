n1=int(input("Ecolha um número para converter: "))
print("[1] Binário [2] Octal [3] Hexadecimal")
n2=int(input("Qual você irá escolher para converter?"))
if n2==1:
    print(f"{bin(n1)[2:]} convertido para bináraio")
elif n2==2:
    print(f"{oct(n1)[2:]} convertido para octal")
else:
    print(f"{hex(n1)[2:]} Convertido para Hexadecimal")