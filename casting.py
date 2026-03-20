def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    Precio = 150
    Descuento = 23.5
    precio_descuento = Precio - Descuento
    cantidad = 3
    print("Precio: " + str(Precio))
    print("Descuento: " + str(Descuento))
    print("Precio con descuento: " + str(precio_descuento))
    Total = precio_descuento * cantidad
    print("Total: " + str(Total))
