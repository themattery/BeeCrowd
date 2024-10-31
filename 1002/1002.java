import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
       Scanner teclado = new Scanner(System.in);
       double raio, n = 3.14159, area;
       
       raio = teclado.nextDouble();
       area = n * Math.pow(raio, 2);
       
       System.out.printf("A=%.4f\n", area);
       
    }
 
}