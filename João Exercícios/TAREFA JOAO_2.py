idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <= 10:
    print("Categoria Infantil")
elif idade >= 11 and idade <= 17:
    print("Categoria Juvenil")
elif idade >= 18:
    print("Categoria Adulto")
else:
    print("Não pode competir")