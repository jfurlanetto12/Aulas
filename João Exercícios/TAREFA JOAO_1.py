nome = input("Digite o nome do produto: ")
valor = int(input("Digite o valor do produto: "))
desconto = valor * 0.15
preco = valor - desconto

print(f"O produto {nome} custava {valor} e com 15% de desconto passará a custar R$ {preco}")