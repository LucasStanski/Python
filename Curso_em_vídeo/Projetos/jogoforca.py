print("**************************")
print("Bem vindo ao jogo de forca")
print("**************************")
palavra_secreta="Abobora"
enforcou=False
acertou=False
while (not enforcou and not acertou):
    chute=str(input("Qual letra? "))
    chute=chute.strip()
    index=0
    for letra in palavra_secreta:
        if(chute.upper())==(letra.upper()):
            print(f"Encontrei a letra {chute} na posição {index}")
        index=index+1
