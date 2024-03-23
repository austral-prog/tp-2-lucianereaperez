def change():
    expense=23.75
    money=100
    print("Ingresar gasto:")
    print(expense)
    print()
    print("Dinero recbido")
    print(money)
    print()
    vuelto =(money-expense)
    print("Vuelto")
    print()
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    print(int((vuelto-int(vuelto))*100)
