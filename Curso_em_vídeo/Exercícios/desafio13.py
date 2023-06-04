salario = float(input('Qual é o salário do funcionário? R$'))
aumento = float(input('Quantos porcento de aumento? '))
novo_sal = salario * ((100 + aumento)/100)
print(f'Um funcionário que ganhava R${salario:.2f}, com {aumento:.0f}% ', end= ''
      f'de aumento, passa a receber R${novo_sal:.2f}')
