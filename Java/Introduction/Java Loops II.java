import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int res= a;
            if(a>=0&&a<=50&&b>=0&&b<=50&&n>=0&&n<=15)
            {
                for (int j = 0; j < n; j++)
            {
                res += (int)(Math.pow(2, j) * b);
                System.out.print(Integer.toString(res)  + ' ');
            }
            }
            System.out.println();
            
        }
        in.close();
    }
}