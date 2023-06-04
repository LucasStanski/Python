expr=str(input("Digite sua expressão: "))
pilha=list
for simb in expr:
    if expr==")":
        pilha.append("(")
    elif expr=="(":
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha)==0:
    print("Sua expressão é válida")
else:
    print("Sua expressão não é válida")
    