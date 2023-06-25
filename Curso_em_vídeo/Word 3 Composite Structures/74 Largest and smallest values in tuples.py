from random import sample
#repetidor=1
#while repetidor !=6:
#    aleatorio=random.randint(0,30)
#    repetidor+=1
#print(aleatorio)

a=tuple(sample(range(10),5))
print(a)
print(f"O menor valor é {min(a)}")
print(f"O maior valor é {max(a)}")
