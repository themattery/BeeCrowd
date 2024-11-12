import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        int cod, numPec;
        double valor, total;
        
        cod = input.nextInt();
        numPec = input.nextInt();
        valor = input.nextDouble();
        total = numPec * valor;
        
        cod = input.nextInt();
        numPec = input.nextInt();
        valor = input.nextDouble();
        total += numPec * valor;
        
        System.out.println(String.format("VALOR A PAGAR: R$ %.2f", total));
 
    }
 
}