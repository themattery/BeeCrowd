import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        
        double raio, volume, pi = 3.14159;
        
        raio = input.nextDouble();
        
        volume = (4.0/3) * pi * Math.pow(raio, 3);
        
        System.out.println(String.format("VOLUME = %.3f", volume));
 
    }
 
}