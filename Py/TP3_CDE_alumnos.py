import os

Alumnos = [
    {'dni': 123456789, 'nombre': 'Juan Pérez', 'nota': 8},
    {'dni': 987654321, 'nombre': 'María Gómez', 'nota': 7},
    {'dni': 456789123, 'nombre': 'Carlos Torres', 'nota': 9},
    {'dni': 321654987, 'nombre': 'Ana López', 'nota': 6},
    {'dni': 654321789, 'nombre': 'Luis Ramírez', 'nota': 10},
    {'dni': 789123456, 'nombre': 'Laura Fernández', 'nota': 8},
    {'dni': 159753486, 'nombre': 'Marta Ruiz', 'nota': 7},
    {'dni': 258741369, 'nombre': 'Pedro Herrera', 'nota': 9},
    {'dni': 369852147, 'nombre': 'Sofía Castro', 'nota': 10},
    {'dni': 147258369, 'nombre': 'Diego Serrano', 'nota': 5},
    {'dni': 753951486, 'nombre': 'Isabel Medina', 'nota': 6},
    {'dni': 486123759, 'nombre': 'Javier Ortega', 'nota': 7},
    {'dni': 951753852, 'nombre': 'Raúl Pérez', 'nota': 8},
    {'dni': 789654123, 'nombre': 'Gabriela Moreno', 'nota': 10},
    {'dni': 321987654, 'nombre': 'Daniela Álvarez', 'nota': 9},
]

"""
Plantilla de alumno: Alumnos
Alumnos = [
    {
        'dni': int,
        'nombre': str:
        'nota': int [0 a 10],
    },
]

"""


def limpiarPantalla() -> None:
    """Limpia el texto de la consola.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def validarEntero(mensaje: str) -> int:
    """Valida que la entrada de un usario sea un numero (entero)
    Esta funcion espera la entrada del usuario
    y no devolvera nada hasta que se ingrese
    un numero entero
    Args:
        mensaje (str): Mensaje que se mostrará al usuario

    """
    while True:
        try:
            return abs(int(input(mensaje)))
        except ValueError:
            print("El dato ingresado no es un número, intenta otra vez.")


def leerNombre(para: str = "") -> str:
    """Leer entrada de un nombre con mensaje variable

    Esta funcion leera una entrada del usuario
    para devolver un nombre, con un minimo de
    1 caracter.

    Args:
        para (str): Nombre de quien.
    """
    nombre = ""
    while True:
        nombre = input(f"Ingrese el nombre {para}: ")
        if len(nombre) > 0:
            nombre = nombre.title()
            break

    return nombre


def leerNota() -> int:
    """Leer entrada de la nota

    Esta funcion leera la entrada del usuario
    y devolvera la edad del alumno correspondiente.
    Considerando un rango de entre:

    0 (incluido) -> 10 (incluido)
    """
    edad = 0
    while True:
        edad = validarEntero("Ingrese la nota del alumno [0 a 10]: ")
        if edad >= 0 and edad <= 10:
            break
    return edad


def leerDni():
    return validarEntero("Ingrese el DNI del alumno: ")


def imprimirAlumno(dato: str, valor) -> None:
    """Imprimira los datos de un alumno
    """
    print(f"{dato.upper()} -> {valor}")


def registrarAlumnos():
    while True:
        print(f"\nAlumno: {len(Alumnos)}")
        dni = leerDni()
        if dni == 0:
            break
        Alumnos.append({
            'dni': dni,
            'nombre': leerNombre(),
            'nota': leerNota()
        })


def listarAlumnos():
    for alumno in Alumnos:
        print()
        for k, v in alumno.items():
            imprimirAlumno(k, v)


def obtenerAlumnoPorDni(dni: int):
    for alumno in Alumnos:
        if alumno['dni'] == dni:
            return alumno


def buscarAlumnoPorDni(dni: int):
    alumno = obtenerAlumnoPorDni(dni)
    if alumno is not None:
        print()
        imprimirAlumno('nombre', alumno['nombre'])
        imprimirAlumno('nota', alumno['nota'])
    else:
        print("Alumno no encontrado.")


def ejecutarOpcion(opcion: int) -> None:
    limpiarPantalla()
    if opcion == 1:
        registrarAlumnos()
    elif opcion == 2:
        listarAlumnos()
        print()
    elif opcion == 3:
        buscarAlumnoPorDni(leerDni())
        print()
    elif opcion == 4:
        ordenarAlumnosPorNombreAscendente(Alumnos)
        print("La lista de alumnos fue ordenada por nombre, de forma ascendente.")


def ordenarAlumnosPorNombreAscendente(alumnos: list) -> list:
    long_alumnos = len(alumnos)
    for i in range(long_alumnos):
        for j in range(0, long_alumnos - i - 1):
            nombre_izq = alumnos[j]['nombre']
            nombre_der = alumnos[j + 1]['nombre']
            if nombre_izq > nombre_der:
                alumnos[j]['nombre'] = nombre_der
                alumnos[j + 1]['nombre'] = nombre_izq
    return alumnos


def menu():
    print("1) Registrar alumnos")
    print("2) Listar todos los alumnos")
    print("3) Buscar un alumno por su dni")
    print("4) Ordenar alumnos")
    print("5) Limpiar pantalla")
    print("0) Salir")

    opcion = validarEntero("- Elige una opción: ")
    if opcion != 0:
        ejecutarOpcion(opcion)
        menu()


limpiarPantalla()
menu()
