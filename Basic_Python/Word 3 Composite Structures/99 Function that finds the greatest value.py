from time import sleep
def numbers(*num):
    print("-="*30)
    print("Analisando os valores passados...")
    for p in num:
        print(f"{p} ",end="")
    print(f",ao todo foram informados {len(num)} numbers.")
    print(f"O maior valor informado é: {max(num)}")
    sleep(5)
print()
numbers(1,5,3,8)
numbers(6,9,25,8,1)
numbers(0)
numbers(2,5)
numbers(45,50,1,4,7,83,6)