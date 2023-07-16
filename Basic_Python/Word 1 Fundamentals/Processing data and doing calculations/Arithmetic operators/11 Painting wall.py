BV = input('Bem Vindo, Pintor!!\nPara descobrir Quantos litros de tinta você precisa pra pintar uma área Pressione ENTER: ')
A = float(input('Dígite a Altura da área a ser pintada: '))
L = float(input('Dígite a Largura da área a ser pintada: '))
R = float(input('De acordo com a embalagem da sua tinta, quanto Metros quadrados ela rende, aproximadamente? '))
T = float(input('Quantos litros tem a sua tinta? '))
Sa = A * L
St = R / T
S = Sa / St
print(f'Você precisa de {S:.2f} Litros de tinta para pintar sua área de {Sa:.3f}M²')