//Switch case to print number between 0-9
import java.util.*;

class d35_switch
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number from 0 - 9: ");
        int n = sc.nextInt();

        switch(n)
        {
            case 0:
                System.out.println("You selected the number 0");
                break;

            case 1:
                System.out.println("You selected the number 1");
                break;
            
            case 2:
                System.out.println("You selected the number 2");
                break;

            case 3:
                System.out.println("You selected the number 3");
                break;

            case 4:
                System.out.println("You selected the number 4");
                break;

            case 5:
                System.out.println("You selected the number 5");
                break;

            case 6:
                System.out.println("You selected the number 6");
                break;

            case 7:
                System.out.println("You selected the number 7");
                break;
            
            case 8:
                System.out.println("You selected the number 8");
                break;

            case 9:
                System.out.println("You selected the number 9");
                break;

            default:
                System.out.println("Incorrect number");
        }
    }
}