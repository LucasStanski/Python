#from math import factorial
#n=int(input("Digite o número para calcular o fatorial: "))
#f=factorial(n)
#print(f"O fatorial de {n} é {f}")

from math import factorial
n=int(input("Digite o número para calcular o fatorial: "))
c=n
f=1
print(f"Calculando {n}!",end=" 14")
while c>0:
    print(f"{c}",end="")
    print(" x " if c>1 else " = ",end="")
    f*=c
    c-=1
print(f"{f}")