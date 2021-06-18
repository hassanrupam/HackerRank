import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int re=0;
        if(N>=2&&N<=20)
        {
           for(int i=1;i<=10;i++)
           {
            re=N*i;  
               System.out.println(N+" x "+i+" = "+re);   
           }
            
        }
        else
            {
            
            System.exit(0);
        }
        
    }
}