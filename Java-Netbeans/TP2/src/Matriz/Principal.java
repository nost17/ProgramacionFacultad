package Matriz;

import java.util.Arrays;
import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int filas = Helper.validarEntero(entrada, "Cantidad de filas de la matriz: ");
        int columnas = Helper.validarEntero(entrada, "Cantidad de columnas de la matriz: ");
        int[][] miMatriz = generarMatriz(filas, columnas);

        imprimirMatriz(miMatriz);
        int numeroBuscado = Helper.validarEntero(entrada, "Elija un numero: ");
        int[] ubicacion = obtenerUbicacion(numeroBuscado, miMatriz);
        if (ubicacion != null) {
            imprimirUbicacion(numeroBuscado, ubicacion);
            String direccion = Helper.validarStringNoVacio(entrada, "De que direccion obtener los numeros? (izq / der)");
            String numerosEncontrados = obtenerNumeroPorDireccion(direccion, numeroBuscado, miMatriz, ubicacion);
            System.out.println(numerosEncontrados);
        } else {
            System.out.println("Numero no encontrado");
        }
    }

    public static void imprimirMatriz(int[][] matriz) {
        System.out.println("Matriz generada de " + matriz.length + "x" + matriz[0].length);
        for (int[] fila : matriz) {
            System.out.println(Arrays.toString(fila));
        }
    }

    public static void imprimirUbicacion(int numero, int[] ubicacion) {
        System.out.print("El numero " + numero + " se encuentra en: ");
        System.out.println("(" + ubicacion[0] + ", " + ubicacion[1] + ")");
    }

    public static boolean[] devolverSiEsLimite(int[] ubicacion, int[][] matriz) {
        boolean[] limites = {false, false};

        if (ubicacion[0] == 0) {
            limites[0] = true; // limite izquierdo (primer elemento)
        }

        if (ubicacion[0] == (matriz[0].length - 1)) {
            limites[1] = true; // limite derecho (ultimo elemento)
        }
        // se utiliza matriz[0], porque es una matriz cuadrada
        // si las filas fueran de diferentes longitudes
        // usar este metodo y en vez de int[] ubicacion
        // pedir int numero
//        for (int f = 0; f < matriz.length; f++) {
//            if (numero == matriz[f][0]) {
//                limites[0] = true; // limite izquierdo (primer elemento)
//            }
//            if (numero == matriz[f][matriz[f].length - 1]) {
//                limites[1] = true; // limite derecho (ultimo elemento)
//            }
//        }
        return limites;
    }

    public static String obtenerNumeroPorDireccion(String direccion, int numero, int[][] matriz, int[] ubicacion) {
        String numerosEncontrados = "Numeros encontrados: ";
        direccion = direccion.toLowerCase().substring(0, 3);
        boolean[] limites = devolverSiEsLimite(ubicacion, matriz);
        // int[] ubicacion = obtenerUbicacion(numero, matriz);

        if ((limites[0] && direccion.equals("izq")) || (limites[1] && direccion.equals("der"))) {
            return "No hay numeros a la derecha/izquierda de la posicion indicada";
        }

        if (direccion.equals("izq")) {
            for (int i = 0; i < ubicacion[0]; i++) {
                numerosEncontrados += matriz[ubicacion[1]][i] + " ";
            }
        } else if (direccion.equals("der")) {
            for (int i = ubicacion[0] + 1; i < matriz[ubicacion[1]].length; i++) {
                numerosEncontrados += matriz[ubicacion[1]][i] + " ";
            }
        } else {
            return "direccion invalida";
        }

        return numerosEncontrados;
    }

    public static int[] obtenerUbicacion(int numero, int[][] matriz) {
        int[] ubicacion = new int[2];

        for (int f = 0; f < matriz.length; f++) {
            for (int c = 0; c < matriz[0].length; c++) {
                if (matriz[f][c] == numero) {
                    ubicacion[0] = c;
                    ubicacion[1] = f;
                    return ubicacion;
                }
            }
        }
        return null;
    }

    public static int generarNumeroAleatorio(int alterar) {
        return (int) (Math.random() * (40 + alterar));
    }

    public static int[][] generarMatriz(int num_filas, int num_columnas) {
        int[][] matriz = new int[num_filas][num_columnas];

        for (int f = 0; f < num_filas; f++) {
            int[] fila = new int[num_columnas];
            for (int c = 0; c < num_columnas; c++) {
                fila[c] = generarNumeroAleatorio(c);
            }
            matriz[f] = fila;
        }

        return matriz;
    }
}
