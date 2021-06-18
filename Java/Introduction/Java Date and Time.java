import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String m = in.next();
        String d = in.next();
        String y = in.next();
        int month= Integer.parseInt(m);
        int day= Integer.parseInt(d);
        int year= Integer.parseInt(y);
        Calendar c = Calendar.getInstance();
		c.set(year, month-1, day);
        String s= new DateFormatSymbols().getWeekdays()[c.get(Calendar.DAY_OF_WEEK)].toUpperCase();
		System.out.println(s);
        in.close();
        
    }
}
