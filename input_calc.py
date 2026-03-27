def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    Base = int(input())
    Altura = int(input())
    print(f"Base: {Base}")
    print(f"Altura: {Altura}")
    print(f"Area: {Base * Altura}")
    print(f"Perimetro: {Base*2 + Altura*2}")