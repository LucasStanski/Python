def leiadinheiro(msg):
    válido=False
    while not válido:
        entrada=str(input(msg)).replace(",",".").strip()
        if entrada.isalpha() or entrada.strip()=="":
            print(f"\033[0;31mERRO: \"{entrada}\" Preço inválido\033[m")
        else:
            válido=True
            return float(entrada)