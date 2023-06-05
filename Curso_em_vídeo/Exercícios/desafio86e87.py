matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma_pares=soma_coluna=maior_valor=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um valor para {l}, {c}: "))
print()
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
        if matriz[l][c]%2==0:
            soma_pares+=matriz[l][c]
    print()
for l in range(0,3):
    soma_coluna+=matriz[l][2]
for c in range(0,3):
    if c==0:
        maior_valor=matriz[1][c]
    elif matriz[1][c]>maior_valor:
        maior_valor=matriz[1][c]
print()
print(f"A soma dos números pares é: {soma_pares}")
print(f"A soma da terceira coluna é: {soma_coluna}")
print(f"O maior valor da segunda linha é: {maior_valor}")
print()