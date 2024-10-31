import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        int a, b, sum;
        Scanner teclado = new Scanner(System.in);
        a = teclado.nextInt();
        b = teclado.nextInt();
        sum = a + b;
        System.out.println("X = " + sum);
        teclado.close();
    }

}