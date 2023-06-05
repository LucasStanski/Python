galera=[]
print()
while True:
    nome=str(input("Digite o nome: "))
    num1=float(input("Digite 1° nota: "))
    num2=float(input("Digite 2° nota: "))
    média=(num1+num2)/2
    galera.append([nome,[num1,num2],média])
    resp=str(input("Quer continuar [S|N]: ")).upper()
    while resp not in "NS":
        resp=str(input("QUER CONTINUAR S ou N: ")).upper()
    if resp in "Nn":
        break
print()
print("="*31)
print("N°         Alunos         Média")
print("="*31)
soma=0
for c in galera:
    print(f"{soma:<10}{c[0]:^10}{c[2]:>10}")
    soma+=1
print()
while True:
    pergunta=int(input("Qual aluno você quer ver as notas (999 FINALIZA): "))
    if pergunta==999:
        print("Finalizando...")
        break
    if pergunta<=len(galera):
        print(f"As notas de {galera[pergunta][0]} são {galera[pergunta][1]}")
print()

