import java.util.Scanner;

public class lab1activity2 {
    public static void main(String args[]) {
        Scanner inputObj = new Scanner(System.in);
        
        System.out.println("Input First number: ");
        String xStr = inputObj.nextLine();
        int x = Integer.parseInt(xStr);
        
        System.out.println("Input Second number: ");
        String yStr = inputObj.nextLine();
        int y = Integer.parseInt(yStr);        
        
        
        System.out.println("\nArithmetic Operation: ");
        float add = x + y;
        System.out.println("Addition x+y: " + add);
        float sub = x - y;
        System.out.println("Subtraction x-y: " + sub);
        float mult = x * y;
        System.out.println("Multiplication x*y: " + mult);
        float div = x/y; 
        System.out.println("Division x/y: " + div);
        float mod = x%y;
        System.out.println("Modulus x%y: " + mod);
        float incre = x+1;
        System.out.println("Increment x++: " + incre);
        float decre = x-1;
        System.out.println("Decrement x--: " + decre);
    }
}
