print("Olá, aqui é o exercito Brasileiro")
n1=int(input("Quantos anos vc tem? "))
if n1==18:
    print("Está na hora de se alistar")
elif n1<18:
    n2=18-n1
    print(f"Faltam {n2} anos para vc se alistar")
else:
    n3=n1-18
    print(f"Éra pra você ter se alistado a {n3} anos atrás")