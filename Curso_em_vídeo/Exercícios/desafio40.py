nota1=float(input("Qual nota você tirou no 1° Trimestre: "))
nota2=float(input("Qual nota você tirou no 2° Trimestre? "))
media=(nota2+nota1)/2
print(f"A média do aluno foi {media:.2f} e o aluno está:")
if media<5.0:
    print("Reprovado")
elif media>6.9:
    print("Aprovado")
else:
    print("Para Recuperação")