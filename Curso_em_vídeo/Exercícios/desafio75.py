num=(int(input("Primeiro valor: ")),
     int(input("Segundo valor: ")),
     int(input("Terceiro valor: ")),
     int(input("Quarto valor: ")))
print(num)
print(f"O valor 9 apareceu {num.count(9)} vezes.")
if 3 in num:
     print(f"O primeiro valor 3 apareceu na {num.index(3+1)}º posição.")
else:
     print("O valor 3 não foi digitado em nenhuma posição.")
print("Os valores pares digitados foram",end=" ")
for n in num:
     if n % 2 ==0:
          print(n,end=" ")