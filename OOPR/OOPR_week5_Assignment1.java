import java.util.Scanner;
public class week_5_Assignment1 {
    public static void main(String args[]) {
        Scanner inputObj = new Scanner(System.in);
        
        System.out.println("Enter first word:");
        String xStr = inputObj.nextLine();
        
        System.out.println("Enter second word:");
        String yStr = inputObj.nextLine();

        System.out.println("Enter third word:");
        String zStr = inputObj.nextLine();

        System.out.println(xStr + " " + yStr + " " + zStr);
    }
}
