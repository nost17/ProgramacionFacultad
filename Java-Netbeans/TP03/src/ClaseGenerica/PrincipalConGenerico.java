package ClaseGenerica;

import java.util.ArrayList;

public class PrincipalConGenerico {

    public static void main(String[] args) {
        
        ArrayList<Integer> numerosEnteros = new ArrayList<>();
        
        numerosEnteros.add(10);
        numerosEnteros.add(24);
        numerosEnteros.add(3);
        numerosEnteros.add(2);
        
        Operaciones.mostrar(numerosEnteros);
        
        ClaseGenerica<Integer> variableEntera = new ClaseGenerica(10);
        System.out.println(variableEntera.getValor());
        
        System.out.println(Operaciones.sumar(variableEntera.getValor(), 4.4));
        
        System.out.println(String.valueOf(1000));
    }
}
