idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Entrada Permitida apenas com acompanhante.")
    print("Foi bom te atender")

else:
    carteira = float(input("Quanto você tem na carteira? "))

    if carteira >= 30:
        print("Ingresso comprado, aproveite o filme!")
        print("Foi bom te atender") 
    else:
        print("Você não tem dinheiro suficiente para comprar o ingresso.")
        print("Foi bom te atender")