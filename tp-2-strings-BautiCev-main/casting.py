def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    Precio = int(input("Precio: "))
    Descuento = float(input("Descuento: "))
    precio_descuento = Precio - Descuento
    cantidad = int(input("Cantidad: "))
    print("Precio: " + Precio.__str__())
    print("Descuento: " + Descuento.__str__())
    print("Precio con descuento: " + precio_descuento.__str__())
    Total = precio_descuento * cantidad
    print("Total: " + Total.__str__())
    pass