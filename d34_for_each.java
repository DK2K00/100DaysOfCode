import java.util.*;

class d34_for_each
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements:");
        int n = sc.nextInt();
        int[] a = new int[n];
        int sum = 0;
        
        System.out.println("Enter the elements: ");
        for(int i = 0; i < n; i++)
        {
            a[i] = sc.nextInt();
            sum += a[i];
        }

        System.out.println("Final sum: " + sum);
    }
}