#num=[]
#for a in range(1,6):
#    valor=int(input(f"Digite o {a}° valor: "))
#    if a==0 or valor>num[-1]:
#        num.append(valor)
#    else:
#        pos=0
#        while pos<len(num):
#            if valor<=num[pos]:
#                num.insert(pos,valor)
#                break
#            pos+=1
#print(f"Os valores digitados em ordem foram {num}")
    
l = [ ]
for x in range(0,5):
    i = float(input(f'Digite o {x+1}º valor: '))
    if x == 0 or i >= l[-1]:
        l.append(i)
        print('Adicionado ao fim da lista.')
    else:
        for y in l:
            if y >= i:
                l.insert(l.index(y),i)
                print(f'Adicionado na posição {l.index(i)} da lista.')
                break
print(f'Os valores digitados em ordem foram {l}')