def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    Precio = int(input())
    Descuento = float(input())
    cantidad = int(input())
    precio_descuento = Precio - Descuento
    print("Precio: " + str(Precio))
    print("Descuento: " + str(Descuento))
    print("Precio con descuento: " + str(precio_descuento))
    Total = precio_descuento * cantidad
    print("Total: " + str(Total))