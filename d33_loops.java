//Fibonacci sequence
import java.util.*;

import jdk.javadoc.internal.doclets.toolkit.resources.doclets;
class d33_loops
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements in sequence: ");
        int n = sc.nextInt();
        
        //For loop
        int a = 0;
        int b = 1;
        int sum = 0;

        for(int i = 0; i < n; i++)
        {
            sum = a + b;
            a = b;
            b = sum;
        }

        System.out.println("For loop fibonacci: " + sum);

        //While loop
        a = 0;
        b = 1;
        sum = 0;
        int i = 0;
       
        while(i < n)
        {
            sum = a + b;
            a = b;
            b = sum;

            i++;
        }

        System.out.println("While loop fibonacci: " + sum);

        //Do while
        a = 0;
        b = 1;
        sum = 0;
        i = 0;
       
        do
        {
            sum = a + b;
            a = b;
            b = sum;

            i++;
        }while(i < n);

        System.out.println("Do while loop fibonacci: " + sum);
    }
}