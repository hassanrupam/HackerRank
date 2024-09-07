import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'insertionSort1' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void insertionSort1(int n, List<Integer> arr) {
     int key = arr.get(n - 1); // The last element to be inserted
        int i = n - 2; // Start checking from the second last element

        // Start shifting elements
        while (i >= 0 && arr.get(i) > key) {
            arr.set(i + 1, arr.get(i)); // Shift element to the right
            printArray(arr); // Print current state of the array
            i--; // Move to the previous element
        }

        arr.set(i + 1, key); // Insert the key at the correct position
        printArray(arr); // Print the final state of the array
    }
    
     // Helper method to print the array
    private static void printArray(List<Integer> arr) {
        System.out.println(arr.stream().map(Object::toString).collect(joining(" ")));
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.insertionSort1(n, arr);

        bufferedReader.close();
    }
}
