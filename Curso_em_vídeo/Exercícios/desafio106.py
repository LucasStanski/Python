from time import sleep
def titulo(msg,cor='\033[:m'):
    print(cor,end='')
    print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))
    print('\033[m')

def leia(texto, tipo='S', tamanho=99):
    """-> Retorna um contedudo recebido pelo teclado onde:
    texto = É o texto apresentado na tela para a inserção dos dados
    tipo = o tipo do valor de retorno pode ser 'i' , 's' ou 'f' onde:
        'i'= para valor inteiro por padrão é string
        's' = para string
        'f' = para float
    tamanho = A quantidade maxima de digitos permitido por padrão é 99"""

    if tipo.upper() == 'S':
        a = str(input(texto)[:tamanho])
    elif tipo.upper() == 'I':
        a = int(input(texto)[:tamanho])
    elif tipo.upper() == 'f':
        a = float(input(texto)[:tamanho])
    return a


#programa principal

while True:
    titulo('SISTEMA DE AJUDA PYHELP','\033[42:38m')
    text = leia('Função ou bibliotec > ')
    if text.upper() =='FIM':
        break
    titulo(f"acessando o manual do comando '{text}'",'\033[46:38m')
    sleep(2)
    print(f'\033[47:30m')
    help(len)