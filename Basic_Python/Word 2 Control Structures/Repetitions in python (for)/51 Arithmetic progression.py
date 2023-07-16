primeiro=int(input("Digite o primero termo: "))
razao=int(input("Digite a razão: "))
decimo=primeiro+(10-1)*razao
for c in range(primeiro, decimo+razao, razao):
    print(f"{c}", end=" ")