jogador = dict()

jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input('Quantas partidas jogou: '))

jogador['gols'] = list()

for i in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['total'] = sum(jogador['gols'])

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} tem {jogador["partidas"]} partidas.')

for c in range(0, jogador['partidas']):
    print(f'   => Na partida {c+1} fez {jogador["gols"][c]}.')
print(f'E fez um total de {jogador["total"]} gols.')