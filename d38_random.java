import java.io.*;
class d38_random
{
    public static void main(String[] args)
    {
        System.out.println(1+2+3+4+"Hello");
        System.out.println("Hello"+1+2+3+4);
        System.out.println(1+2+3+4+"Hello"+1+2+3+4);
        System.out.println(1+2+3+4+"Hello"+(1+2+3+4));

        Object obj1;
        
        if(true)
        {
            obj1 = new Integer(10);
        }
        else
        {
            obj1 = new Float(20.0);
        }

        System.out.println(obj1);

        Object obj2 = true ? new Integer(10) : new Float(20.0);
        System.out.println(obj2);
    }
}
