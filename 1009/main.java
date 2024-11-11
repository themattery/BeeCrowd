import java.io.IOException;
import java.util.Scanner;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        String nomeFunc;
        double salarioFixo, totalVendas, salarioFinal;
        
        Scanner input = new Scanner(System.in);
        nomeFunc = input.nextLine();
        salarioFixo = input.nextDouble();
        totalVendas = input.nextDouble();
        
        salarioFinal = salarioFixo + totalVendas*0.15;
        
        System.out.println(String.format("TOTAL = R$ %.2f", salarioFinal));
 
    }
 
}