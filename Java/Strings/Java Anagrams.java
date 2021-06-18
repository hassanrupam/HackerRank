import java.util.Scanner;

public class Solution {

       static boolean isAnagram(String a, String b) {
        // Complete the function
        String q= a.toLowerCase();
        String r= b.toLowerCase();
        
        char[] arr1= q.toCharArray();
        char[] arr2= r.toCharArray();
        
        if(arr1.length!=arr2.length)
        {
            return false;
        }
        else
        {
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        
        if(Arrays.equals(arr1,arr2))
        {
            return true;
        }
        else
        {
            return false;
        }
        }
        
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}