import time
x=time.localtime()
x=x[0]
detalhes={"Nome":str(input("Digite o nome: ")),"Idade":int(input("Ano de nascimento: ")),"CTPS":int(input("Número da carteira de trabalho (0 se não tiver CTPS): "))}
idade=x-detalhes["Idade"]
detalhes["Idade"]=idade
if detalhes["CTPS"]==0:
    for k,v in detalhes.items():
        print(f"{k} tem o valor {v}")
else:
    detalhes["Contratação"]=int(input(f"Em qual ano você foi contratado {detalhes['Nome']}: "))
    detalhes["Salário"]=float(input(f"Qual é seu salário {detalhes['Nome']}: "))
    Passo1=x-detalhes["Contratação"]
    Passo2=35-Passo1
    Passo3=Passo2+idade
    detalhes["Aposentadoria"]=Passo3
    for k,v in detalhes.items():
        print(f"{k} tem o valor {v}")