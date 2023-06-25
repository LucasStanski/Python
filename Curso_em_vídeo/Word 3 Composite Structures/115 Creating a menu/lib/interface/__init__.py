def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mEntrada de dados interrompidas pelo usuário\033[m")
            return 0
        else:
            return n 

def linha(tam=42):
    return "="*tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))   
    print(linha())

def menu(Vetor):
    cabeçalho("MENU PRINCIPAL")
    c=1
    for item in Vetor:
        print(f"{c} - {item}")
        c+=1
    print(linha())
    opc=leiaint("Sua Opção: ")
    return opc