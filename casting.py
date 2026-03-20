def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    Precio = int(input("Precio: "))
    Descuento = float(input("Descuento: "))
    precio_descuento = Precio - Descuento
    cantidad = int(input("Cantidad: "))
    print("Precio: " + str(Precio))
    print("Descuento: " + str(Descuento))
    print("Precio con descuento: " + str(precio_descuento))
    Total = precio_descuento * cantidad
    print("Total: " + str(Total))
    pass
casting()