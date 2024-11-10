import java.io.IOException;
import java.util.Scanner;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        int num, horasTrab;
        double valorHora, salario;
        
        Scanner input = new Scanner(System.in);
        
        num = input.nextInt();
        horasTrab = input.nextInt();
        valorHora = input.nextDouble();
        
        salario = horasTrab * valorHora;
        
        System.out.println("NUMBER = " + num);
        System.out.println(String.format("SALARY = U$ %.2f" , salario));
    }
 
}