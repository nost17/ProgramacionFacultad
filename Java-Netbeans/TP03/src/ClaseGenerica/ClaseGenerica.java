
package ClaseGenerica;

public class ClaseGenerica<T> {
    private T valor;

    public ClaseGenerica() {
    }

    public ClaseGenerica(T valor) {
        this.valor = valor;
    }

    public T getValor() {
        return valor;
    }

    public void setValor(T valor) {
        this.valor = valor;
    }
}
