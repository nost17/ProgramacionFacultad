import os
Mascotas: list[list] = [
    ["Fido", "P", 5, 12.5, "S",
        [12345678, "Juan Perez", "555-1234", "Calle Falsa 123"]],
    ["Miau", "G", 3, 4.2, "C",
        [12345678, "Juan Perez", "555-5678", "Avenida Siempre Viva 742"]],
    ["Hammy", "H", 1, 0.3, "E",
        [11223344, "Luis Alvarez", "555-9101", "Boulevard de los Sueños Rotos 404"]],
    ["Rex", "P", 7, 18.0, "S",
        [33445566, "Carlos Martinez", "555-1122", "Camino de los Gigantes 505"]],
    ["Luna", "G", 2, 3.8, "E",
        [99887766, "Sofia Lopez", "555-3344", "Callejón del Viento 808"]],
    ["Speedy", "H", 4, 0.5, "S",
        [55667788, "Ana Torres", "555-5566", "Avenida del Sol 909"]],
    ["Speedy", "P", 4, 7, "S",
        [55667788, "Sofia Castro", "545-2227", "Avenida del valle 200"]]
]

dato_por_letra = {
    'P': 'Perro',
    'G': 'Gato',
    'H': 'Hamster',
    'S': 'Saludable',
    'E': 'Enfermo',
    'C': 'Control',
}


"""
Plantilla de mascotas:
    mascota = [
        'Nombre': str,
        'Especie': ( 'P'= Perro, 'G'= Gato, 'H'= Hamster ),
        'Edad': int [0,20],
        'Peso': float,
        'Estado de salud': ( 'S'=Saludable, 'E'=Enfermo, 'C'=Control ),
        'Dueño': [
            'Dni': int,
            'Nombre': str,
            'Telefono': int,
            'Dirección': str
        ],
    ]
"""

# -------


def validarEntero(mensaje: str) -> int:
    """Valida que la entrada de un usario sea un numero (entero)
    Esta funcion espera la entrada del usuario
    y no devolvera nada hasta que se ingrese
    un numero entero
    Args:
        mensaje (str): Mensaje que se mostrar al usuario

    """
    numero = 0
    while True:
        try:
            numero = int(input(mensaje))
            break
        except ValueError:
            print("El dato ingresado no es un número, intenta otra vez.")
    return numero


def validarFlotante(mensaje: str) -> float:
    """Valida que la entrada de un usario sea un numero (flotante)
    Esta funcion espera la entrada del usuario
    y no devolvera nada hasta que se ingrese
    un numero valido
    Args:
        mensaje (str): Mensaje que se mostrar al usuario

    """
    numero: float = 0
    while True:
        try:
            numero = float(input(mensaje))
            break
        except ValueError:
            print("El dato ingresado no es un número, intenta otra vez.")
    return numero


def limpiarPantalla() -> None:
    """Limpia el texto de la consola.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def imprimirDato(dato: str, valor) -> None:
    print(f"{dato.upper()} -> {valor}")


def imprimirDueño(dueño: list) -> None:
    imprimirDato("dni", dueño[0])
    imprimirDato("nombre", dueño[1])
    imprimirDato("telefono", dueño[2])
    imprimirDato("dirección", dueño[3])


def imprimirMascota(mascota: list, id="", dueño=True, edad=True, peso=True, salud=True) -> None:
    print("----- MASCOTA", id, "-----")
    imprimirDato("nombre", mascota[0])
    imprimirDato("especie", dato_por_letra.get(mascota[1]))
    if edad:
        imprimirDato("edad", f"{mascota[2]} años")
    if peso:
        imprimirDato("peso", f"{mascota[3]} kg")
    if salud:
        imprimirDato("estado de salud", dato_por_letra.get(mascota[4]))
    if dueño:
        print("----- DUEÑO -------")
        imprimirDueño(mascota[5])
    print()

# -------


def leerNombre(para: str) -> str:
    """Leer entrada de un nombre con mensaje variable

    Esta funcion leera una entrada del usuario
    para devolver un nombre, con un minimo de
    3 caracteres, y un maximo de 20.

    Args:
        para (str): Nombre de quien.
    """
    nombre = ""
    while True:
        nombre = input(f"Ingrese el nombre {para}: ")
        if len(nombre) > 3 and len(nombre) <= 20:
            nombre = nombre.title()
            break

    return nombre


def leerEspecie() -> str:
    """Leer entrada de la especie

    Esta funcion leera la entrada de usuario
    para devolver una especie de la mascota.

    Siendo que las opciones son:

    **P** = Perro,

    **G** = Gato,

    **H** = Hamster
    """
    especie = ""
    while True:
        print("Considere -> 'P'= Perro, 'G'= Gato, 'H'= Hamster ")
        especie = input("Ingrese la especie: ").upper()
        if especie == "P" or especie == "G" or especie == "H":
            break
    return especie


def leerEdad() -> int:
    """Leer entrada de la edad

    Esta funcion leera la entrada del usuario
    y devolvera la edad de la mascota.
    Considerando una edad de entre:

    0 (incluido) -> 20 (incluido)
    """
    edad = 0
    while True:
        edad = validarEntero("Ingrese la edad de la mascota [0 a 20 años]: ")
        if edad >= 0 and edad <= 20:
            break
    return edad


def leerPeso() -> float:
    """Leer entrada del peso

    Esta funcion leera la entrada del usuario
    y devolvera el peso de la mascota.
    """
    peso = 0.0
    while True:
        peso = validarFlotante("Ingrese el peso de la mascota: ")
        if peso > 0:
            break
    return peso


def leerEstadoDeSalud() -> str:
    """Leer entrada del estado de salud

    Esta funcion leera la entrada de usuario
    para devolver un estado de salud de la mascota.

    Siendo que las opciones son:

    **S** = Saludable,

    **E** = Enfermo,

    **C** = Control
    """
    especie = ""
    while True:
        print("Considere -> 'S'= Saludable, 'E'= Enfermo, 'C'= Control ")
        especie = input("Ingrese el estado de salud de la mascota: ").upper()
        if especie == "S" or especie == "E" or especie == "C":
            break
    return especie


def obtenerDueñoDni(dni: int):
    for mascota in Mascotas:
        if mascota[5][0] == dni:
            return mascota[5]


def crearDueño() -> list:
    """Leera multiples entradas y creara un dueño

    Esta funcion leera los datos del dueño de
    una mascota

    **Datos:**
        >>> dni :int
        nombre: str
        telefono: int
        dirección: str
    
    En caso de que el DNI ingresado coincida con uno
    de la lista `Mascotas`, entonces se le preguntará
    al usuario si desea utilizar los datos encontrados
    o ingresar otros (no reemplazar los datos mostrados) 
    """
    dni = validarEntero("Ingrese el DNI del dueño: ")
    coincidencia = obtenerDueñoDni(dni)
    pedir_datos = True
    if coincidencia is not None:
        print("Hay una coincidencia encontrada:")
        imprimirDueño(coincidencia)
        usar_datos_encontrados = input(
            "Usar los datos encontrados? (s/n): ").lower()
        if usar_datos_encontrados == "s":
            pedir_datos = False
            nombre = coincidencia[1]
            telefono = coincidencia[2]
            direccion = coincidencia[3]
    if pedir_datos:
        nombre = leerNombre("del dueño")
        telefono = validarEntero("Ingrese el numero de telefono: ")
        direccion = input("Ingrese la direción del dueño: ")

    return [dni, nombre, telefono, direccion]


def agregarMascota() -> None:
    """Añadir una mascota

    Esta funcion recibira los datos necesarios,
    creara una mascota y la añadira a la lista
    mayor de `Mascotas`
    """
    nombre = leerNombre("de la mascota")
    especie = leerEspecie()
    edad = leerEdad()
    peso = leerPeso()
    salud = leerEstadoDeSalud()
    dueño = crearDueño()
    mascota = [nombre, especie, edad, peso, salud, dueño]
    Mascotas.append(mascota)


def buscarMascotaNombre(nombre: str) -> list:
    """Busca mascotas por el nombre

    Esta funcion buscara mascotas con el nombre
    solicitado y devolvera una lista con
    las coincidencias

    Args:
        nombre (str): Nombre de la mascota a buscar
    """
    nombre = nombre.title()
    encontrados = [mascota for mascota in Mascotas if mascota[0] == nombre]
    return encontrados


def actualizarSalud() -> None:
    """Acutalizar estado de salud de una mascota

    Esta funcion solicitara al usuario un nombre
    y buscara entre la lista de mascotas, debido
    a que pueden haber multiples coincidencias
    se le preguntara al usuario cual mascota le pertenece

    En caso de que solo haya 1 coincidencia, se
    pedira una confirmacion de igual manera 
    """

    mascotas = buscarMascotaNombre(leerNombre("de la mascota"))
    if len(mascotas) > 1 and mascotas:
        for id, mascota in enumerate(mascotas):
            imprimirMascota(mascota, str(id))
        id_elegido = validarEntero("Elige tu mascota por id (ej: 0): ")
        if mascotas[id_elegido]:
            mascotas[id_elegido][4] = leerEstadoDeSalud()
    else:
        imprimirMascota(mascotas[0], dueño=False)
        confirmacion = input("¿Es tu mascota?: ").lower()
        if confirmacion == "s":
            mascotas[0][4] = leerEstadoDeSalud()
        else:
            print("Mascota no encontrada :/")


def listarMascotasPorDueño(dni: int) -> None:
    """Imprime los datos de las mascotas de un dueño
    en especifico.
    """
    for mascota in Mascotas:
        if mascota[5][0] == dni:
            imprimirMascota(mascota, dueño=False)


def listarMascotasEnfermas() -> None:
    """Imprimira las mascotas enfermas
    """
    for id, mascota in enumerate(Mascotas):
        if mascota[4] == "E":
            imprimirMascota(mascota, str(id), edad=False,
                            peso=False, salud=False)


def ejecutarOpcion(opcion: int) -> None:
    limpiarPantalla()
    if opcion == 1:
        agregarMascota()
    elif opcion == 2:
        for _mascota in buscarMascotaNombre(leerNombre("de la mascota")):
            imprimirMascota(_mascota)
    elif opcion == 3:
        actualizarSalud()
    elif opcion == 4:
        listarMascotasPorDueño(validarEntero("Ingrese DNI del dueño: "))
    elif opcion == 5:
        listarMascotasEnfermas()
    elif opcion == 6:
        limpiarPantalla()


def menu():
    print("1) Agregar mascota")
    print("2) Buscar una mascota por su nombre")
    print("3) Actualizar el estado de salud de una mascota")
    print("4) Listar mascotas de un dueño")
    print("5) Listar mascotas enfermas")
    print("6) Limpiar pantalla")
    print("0) Salir")

    opcion = validarEntero("- Elige una opción: ")
    if opcion != 0:
        ejecutarOpcion(opcion)
        menu()


limpiarPantalla()
menu()
