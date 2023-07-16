n1=int(input("Primeiro número: "))
n2=int(input("Segundo número: "))
n3=int(input("Terceiro número: "))
if n1>n2 and n1>n3:
    print(f"O primeiro número que é {n1} é maior")
elif n2>n1 and n2>n3:
    print(f"O segundo número que é {n2} é maior")
elif n3>n1 and n3>n2:
    print(f"O terceiro número que é {n3} é maior")
if n1<n2 and n1<n3:
    print(f"O primeiro número que é {n1} é menor")
elif n2<n1 and n2<n3:
    print(f"O segundo número que é {n2} é menor")
elif n3<n1 and n3<n2:
    print(f"O terceiro número que é {n3} é menor")        
