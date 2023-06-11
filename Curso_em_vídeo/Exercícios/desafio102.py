def fatorial(a,show):
    from math import factorial
    if show==False:
        print("-"*30)
        print(f'O fatorial de {a} é {factorial(a)}')
    if show==True:
        f=1
        while a>0:
            print(f"{a}",end="")
            print(" x " if a>1 else " = ",end="")
            f*=a
            a-=1
        print(f"{f}")
print(fatorial(5,show=True))
