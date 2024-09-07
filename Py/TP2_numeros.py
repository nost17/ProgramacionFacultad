"""
1. Numeros positivos
2. 5 numeros
3. Separados por espacio
"""

import os


def miniMaxSum(arr: list) -> str:
    sumas = []

    # sumas = [ sum(arr) - num for num in arr ]
    for num in arr:
        sumas.append(sum(arr) - num)

    return f"{min(sumas)} {max(sumas)}"


def pedirNumeros(mensaje: str) -> list:
    while True:
        try:
            return list(map(int, input(mensaje).split()))
        except ValueError:
            print("Solo se admiten numeros.")


def validarLongitudLista(lista: list, long: int = 5) -> bool:
    return (len(lista) == long)


def validarPositivos(lista: list) -> bool:
    for num in lista:
        if num < 0:
            return False
    return True


def main(limpiar=True):
    if limpiar:
        os.system("cls")
    else:
        print("Intente otra vez.")

    numeros = pedirNumeros("Ingrese 5 números separados por espacios: ")
    son_positivos = validarPositivos(numeros)

    if validarLongitudLista(numeros) and son_positivos:
        print(miniMaxSum(numeros))
    elif not (son_positivos):
        print("Debe ingresar solo numeros positivos.")
        main(False)
    else:
        print("La cantidad de numeros que debe ingresar es de 5")
        main(False)


main()
