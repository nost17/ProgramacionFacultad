package pilas1;

public class StackChar{
	private final int maximoTamanio=100;
	private char [] datos;
	private int cuenta;
	
	
	public StackChar(int tamanio) {
		datos=new char[tamanio];
	}
	
	public StackChar() {
		this.datos=new char[maximoTamanio];
		this.cuenta=0;
	}
	
	public void Push(char elemento) {
		if (this.cuenta>=maximoTamanio) {
			throw new RuntimeException("pila llena idiota");
			
		}
		
		this.datos[this.cuenta]=elemento;
		++this.cuenta;
		
		
	}
	public char Pop() {
		if (this.isEmpy()) {//no comparo cuenta , sino m evalgo del metodo de 
			//validacion si mi cuenta==0, esta es una buena practica de programacion
			throw new RuntimeException("tu pila esta vacia idiot");
			
		}
		--this.cuenta;
		return this.datos[this.cuenta];
		//no se saca el elemento ya que devolvemos una copia del valor y en el proxi push
		//se sobrescribira en la posicion del elemetno a salir
		
	}
	
	
	public char Peek() {
		if(this.isEmpy()) {
			throw new RuntimeException("pila vacia");
		}
		return this.datos[this.cuenta-1];
	}
	
	public boolean isEmpy() {
		return this.cuenta<=0;
	}
	
	
	
	
	
	
}
