def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recbido")
    print(money)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    print(int(((money - expense)- int(money - expense)) * 100))
