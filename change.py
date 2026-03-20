def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingresar gasto: "))
    print("Ingresar gasto:")
    print(gasto)
    ingreso = int(input("Dinero recibido "))
    print("Dinero recibido")
    print(ingreso)
    print("")
    Vuelto = ingreso - gasto
    print("Vuelto")
    print("")
    Pesos = int(Vuelto)
    Centavos = Vuelto * 100 - Pesos * 100
    print("Pesos:")
    print(Pesos)
    print("Centavos:")
    print(int(Centavos))
    pass
change()
