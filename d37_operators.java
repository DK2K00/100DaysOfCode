class d37_operators
{
    public static void main(String[] args)
    {
        int a = 10, b = 20;
        int c;

        c = a + b;
        System.out.println("a + b = " + c);

        c = a - b;
        System.out.println("a - b = " + c);
        
        c = a * b;
        System.out.println("a * b = " + c);

        c = a / b;
        System.out.println("a / b = " + c);

        c = a % b;
        System.out.println("a % b = " + c);


        a = a << 2;
        System.out.println("a << 2 = " + a);
    }    
}