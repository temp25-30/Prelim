import java.util.Scanner;
class Main {
    static boolean run = true;
    static void gCalc(){
        Scanner inputObj = new Scanner(System.in);
        float aveGrade;
        char letterGrade;

        //Java grade
        System.out.println("Input Java Grade.");
        
        String JStr = inputObj.nextLine();
        int gradeJava = Integer.parseInt(JStr);

        //C grade
        System.out.println("Input C Grade: ");
        
        String CStr = inputObj.nextLine();
        int gradeC = Integer.parseInt(CStr);

        //Database Handling grade
        System.out.println("Input Database Handling Grade: ");
        
        String DBStr = inputObj.nextLine();
        int gradeDB = Integer.parseInt(DBStr);
        
        //average
        aveGrade = (gradeJava + gradeC + gradeDB);
        
        if(aveGrade/3 >= 90){
            letterGrade = 'A';
        }
        else if(aveGrade/3 >= 80){
            letterGrade = 'B';
        }
        else if(aveGrade/3 >= 74){
            letterGrade = 'C';
        }
        else{
            letterGrade = 'F';
        }
        
        System.out.println("Output: " + letterGrade);
        System.out.println("The average of the student is " + aveGrade/3 + " so the student's grade is: " + letterGrade);   
        
        System.out.println("\nWould you like to use the prgram again? (YES / NO)");
        String ansStr = inputObj.nextLine(); 
        if("NO".equals(ansStr)){
                run = false;
                System.out.println("Program Terminated. Thank you!");
            }
        else if("YES".equals(ansStr)){
                gCalc();
            }
    }
    
    public static void main(String[] args) {
        while(run){
            gCalc();      
        }
    }
}
