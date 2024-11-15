import java.io.IOException;
import java.util.Scanner;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        int km;
        double lit, res;
        
        km = input.nextInt();
        lit = input.nextDouble();
        
        res = km/lit;
        
        System.out.println(String.format("%.3f km/l", res));
        
        
    }
 
}