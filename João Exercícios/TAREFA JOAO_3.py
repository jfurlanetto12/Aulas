codigo = int(input("Digite um numero:"))

match codigo:
    case 1:
        print("Água de coco")
    case 2:
        print("Suco de laranja")
    case 3:
        print("Açaí na tigela")
    case _:
        print("Opção inválida, digite um número de 1 a 3")