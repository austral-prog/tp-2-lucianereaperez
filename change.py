def change():
    expense=23.75
    money=100
    print("Ingresar gasto:")
    print(expense)
    print("")
    print("Dinero recbido")
    print(money)
    print("")
    vuelto=(money-expense)
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(vuelto-0.25))
    print("Centavos:")
    centavos=((vuelto-76)*100)
    print(int(centavos))
    
