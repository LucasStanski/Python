galera={}
print()
galera["nome"]=str(input("Digite o nome: "))
galera["média"]=float(input(f"Digite a média de {galera['nome']}: "))
print()
if galera["média"] >=70:
    galera["situação"]="Aprovado"
elif galera["média"] >=50 <=69:
    galera["situação"]="Recuperação"
else:
    galera["situação"]="Reprovado"
for k,v in galera.items():
    print(f"{k} é {v}")
print()
print(f"Bons estudos {galera['nome']}!!!")
print()

#4 Lines
#aluno = {'nome': str(input('Nome: ')), 'média': float(input('Digite a média: '))}
#aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'reprovado' if aluno['média'] <6 else 'recuperação'
#for key, value in aluno.items():
#	print(f'{key}:', value)