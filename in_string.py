def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    Nombre = input("Ingrese nombre: ").lower()
    a = "a" in Nombre
    e = "e" in Nombre
    i = "i" in Nombre
    o = "o" in Nombre
    u = "u" in Nombre
    print(f"Contiene a: {a}")
    print(f"Contiene e: {e}")
    print(f"Contiene i: {i}")
    print(f"Contiene o: {o}")
    print(f"Contiene u: {u}")