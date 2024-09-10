package Prueba;

import Matriz.Helper;
import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        int numeros[] = new int[5];
        numeros[0] = 10;
        numeros[1] = 10;
        numeros[2] = 10;
        numeros[3] = 10;
        System.out.println(numeros.length);
//        Scanner entrada = new Scanner(System.in);
//        int longitudContraseña = leerLongitudContraseña(entrada);
//        boolean mayusculas = verificacionDeOpciones(entrada, "mayusculas");
//        boolean minusculas = verificacionDeOpciones(entrada, "minusculas");
//        boolean numeros = verificacionDeOpciones(entrada, "numeros");
//        boolean caracteresEspeciales = verificacionDeOpciones(entrada, "caracteres especiales");
//
//        String abecedario = "abcdefghijklmnopqrstuvwxyz";
//        String abecedarioMayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
//        String listaNumeros = "123456789";
//        String especiales = "({)[}|@·#]";
//
//        String clave = new String();
//        for (int i = 0; i < longitudContraseña; i++) {
//            String caracteres = "";
//            if (mayusculas) {
//                caracteres += abecedarioMayusculas;
//            }
//            if (minusculas) {
//                caracteres += abecedario;
//            }
//            if (numeros) {
//                caracteres += listaNumeros;
//            }
//            if (caracteresEspeciales) {
//                caracteres += especiales;
//            }
//            clave += caracteres.charAt( (int) (Math.random() * caracteres.length() ) );
//        }
//
//        System.out.println(clave);
    }

    public static int leerLongitudContraseña(Scanner entrada) {
        int longitudContrasenia;
        do {
            longitudContrasenia = Helper.validarEntero(entrada, "Ingrese con cuantos caracteres tendra la cntraseña");
            if (!(longitudContrasenia > 0)) {
                System.out.println("El numero debe ser positivo");
            } else {
                break;
            }

        } while (true);
        return longitudContrasenia;
    }

    public static boolean verificacionDeOpciones(Scanner entrada, String opcion) {
        boolean confirmacion = false;

        System.out.print("Desea incluir " + opcion + "?: ");
        String pregunta = entrada.nextLine();
        pregunta = pregunta.toLowerCase();

        if (pregunta.equals("s") || pregunta.equals("si")) {
            confirmacion = true;
        }

        return confirmacion;
    }

}
