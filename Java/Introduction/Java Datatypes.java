import java.util.*;
import java.io.*;



class Solution{
    public static void main(String []argh)
    {



        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        String[] arr= new String[t];
        sc.nextLine();
        for(int i=0;i<t;i++)
        {
            arr[i] =  sc.nextLine();
        }
        
        

        for(int i=0;i<t;i++)
        {

            try
            {
               long a= Long.parseLong(arr[i]);
                System.out.println(arr[i]+" can be fitted in:");
                if(a>=-128 && a<=127)
                {
                    System.out.println("* byte \n* short \n* int \n* long");
                }
                else if(  a >= -32768 && a <= 32767 )
                {
                    System.out.println("* short \n* int \n* long"); 
                }
                else if( a >= -2147483648 && a <= 2147483647 )
                {
                    System.out.println("* int \n* long");
                }
                else if( a >= -9223372036854775808l && a <= 9223372036854775807l )
                {
                    System.out.println("* long");
                }
                
            }
            catch(Exception e)
            {
                System.out.println(arr[i]+" can't be fitted anywhere.");
            }

        }
    }
}
