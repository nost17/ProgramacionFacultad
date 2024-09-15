# En un torneo de artes marciales en el mundo de Dragon Ball, se encuentran listados los participantes con
# su Nombre, Transformación y Nivel de poder.
# participantes = [ [“Goku”,”Kaioken”, 10001], ["Vegeta",”Super Saiyajin” 8900], ["Gohan", “Beast”,12000],
# ["Piccolo", “Namekiano”,7000], ["Freezer",”Black”, 9500] ]
#   a. Cree un proyecto en Gitlab y suba la resolución del algoritmo en la rama main.
#   b. Ordenar la lista de participantes en forma ascendente o descendente por nivel de poder con el
#   método de selección.
#   c. Ordenar la lista de participantes en forma descendente por Transformación mostrando solamente
#   los participantes que nivel de poder superior a 9000 utilizando el método de inserción.


def MetodoDeSeleccion(Participantes):
    for i in range(len(Participantes)):
        indiceMenorValor = i
        for j in range(i + 1, len(Participantes)):
            if Participantes[j][2] < Participantes[indiceMenorValor][2]:
                indiceMenorValor = j
        Participantes[i], Participantes[indiceMenorValor] = (
            Participantes[indiceMenorValor],
            Participantes[i],
        )
    return Participantes


def MetodoDeInsercion(Participantes):
    for i in range(1, len(Participantes)):
        indiceMenorValor = i
        MenorValor = Participantes[i]
        while (
            indiceMenorValor > 0
            and MenorValor[2] < Participantes[indiceMenorValor - 1][2]
        ):
            Participantes[indiceMenorValor] = Participantes[indiceMenorValor - 1]
            indiceMenorValor -= 1
        Participantes[indiceMenorValor] = MenorValor
    return Participantes


def MetodoDeBurbuja(Participantes):
    for i in range(len(Participantes)):
        for j in range(0, len(Participantes) - i - 1):
            if Participantes[j][2] > Participantes[j + 1][2]:
                Participantes[j][2], Participantes[j + 1][2] = (
                    Participantes[j + 1][2],
                    Participantes[j][2],
                )
    return Participantes


# Principal
Participantes = [
    ["Goku", "Kaioken", 10001],
    ["Vegeta", "Super Saiyajin", 8900],
    ["Gohan", "Beast", 12000],
    ["Piccolo", "Namekiano", 7000],
    ["Freezer", "Black", 9500],
]
print("Metodo de Burbuja :", MetodoDeBurbuja(Participantes.copy()))
print("Metodo de seleccion : ", MetodoDeSeleccion(Participantes.copy()))
print("Metodo de insercion : ", MetodoDeInsercion(Participantes.copy()))
