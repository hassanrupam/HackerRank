import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
         Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // Write your code here.
        s=s.trim();
        if(s.length()==0)
        {
        System.out.println("0");
        }
        else
        {
        
        String[] out= s.split("[^a-zA-Z]+");
        System.out.println(out.length);
        
        for(int i=0;i<out.length;i++)
        {
        System.out.println(out[i]);
        }
        }
        
        scan.close();
    }
}
