lista=[]
continuar=""
while continuar not in "SNsn":
        continuar=str(input("Vai querer continuar S/N: "))
    if continuar in "Ss":
        continuar=" "
    if continuar in "Nn":
        print("Finalizando...")
            break
