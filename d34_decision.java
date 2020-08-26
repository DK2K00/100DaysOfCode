//Greatest of three numbers
import java.util.*;

class d34_decision
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a,b,c;

        System.out.println("Enter the value of three numbers: ");
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        int max;

        if(a > b && a > c)
        {
            max = a;
            System.out.println("a is the largest number");
            System.out.println("Number is: " + a);
        }
        else if(b > a && b > c)
        {
            max = b;
            System.out.println("b is the largest number");
            System.out.println("Number is: " + b);
        }

        else
        {
            max = c;
            System.out.println("c is the largest number");
            System.out.println("Number is: " + c);
        }
    }   
}