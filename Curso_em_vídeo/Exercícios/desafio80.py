num=[]
for a in range(1,6):
    valor=int(input(f"Digite o {a}° valor: "))
    if a==0 or valor>num[-1]:
        num.append(valor)
    else:
        pos=0
        while pos<len(num):
            if valor<=num[pos]:
                num.insert(pos,valor)
                break
            pos+=1
print(f"Os valores digitados em ordem foram {num}")
    
    