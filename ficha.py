def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    Nombre = input().strip()
    email = input()
    nota1 = input()
    nota2 = input()
    nota3 = input()
    iniciales = Nombre.find(" ")
    dominio = email.find("@")
    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")
    print(f"Nombre: {Nombre.title()}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(Nombre)}")
    print(f"Iniciales: {Nombre[0].upper()}{Nombre[iniciales+1].upper()}")
    print(f"Usuario: {Nombre[iniciales+1:len(Nombre)].lower()}.{Nombre[0:iniciales].lower()}")
    print(f"Email valido: {"@" in email}")
    print(f"Dominio: {email[dominio+1:len(email)].lower()}")
    print(f"Nombre para archivo: {Nombre.replace(" ", "_").title()}")
    print(f"Cantidad de a: {Nombre.lower().count("a")}")
    print(f"Codigo secreto: {Nombre[::-1].upper()}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {int(nota1)+int(nota2)+int(nota3)}")
    print(f"Promedio: {(float(nota1)+float(nota2)+float(nota3))/3}")
    print(f"Promedio entero: {(int(nota1)+int(nota2)+int(nota3))//3}")
    print("="*24)