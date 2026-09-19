import java.util.Scanner;
public class week_5_Assignment2 {
    public static void main(String args[]) {
        Scanner inputObj = new Scanner(System.in);
        
        System.out.println("Enter first number:");
        String xStr = inputObj.nextLine();
        int x = Integer.parseInt(xStr);
        
        System.out.println("Enter second number:");
        String yStr = inputObj.nextLine();
        int y = Integer.parseInt(yStr);
        
        System.out.println("Enter third number:");
        String zStr = inputObj.nextLine();
        int z = Integer.parseInt(zStr);
        
        int highest = x;
        
        if(y>highest){
            highest = y;
        }
        if(z>highest){
            highest = z;
        }
        
        
        System.out.println("The highest number is:" + highest);
    }
}
