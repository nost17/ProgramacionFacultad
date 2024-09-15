package ClaseGenerica;

import java.util.ArrayList;

public class Operaciones {

    public static <T extends Number> double sumar(T numero1, T numero2) {
        double resultado = numero1.doubleValue() + numero2.doubleValue();
        return resultado;
    }
    
    public static <T> void mostrar(ArrayList<T> arreglo){
        for (T elemento: arreglo) {
            System.out.println(elemento);
        }
    }
}
