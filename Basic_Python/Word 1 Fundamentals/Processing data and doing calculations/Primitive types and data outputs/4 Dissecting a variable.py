a=input("Digite qualquer coisa: ")
print(f"O tipo primitivo dessa variavel é {type(a)}")
print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfábetico? ", a.isalpha())
print("É alfanumerico? ", a.isalnum())