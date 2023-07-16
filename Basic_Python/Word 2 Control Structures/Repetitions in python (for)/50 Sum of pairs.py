s=0
p=0
for o in range(0,6):
    n = int(input("Digite um número: "))
    if n%2==0:
        s+=n
    if n%2==1:
        p+=n
print(f"Soma dos numeros pares {s}")
print(f"Soma dos numeros impares {p}")
