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
     * Complete the 'insertionSort2' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void insertionSort2(int n, List<Integer> arr) {
    for (int i = 1; i < n; i++) {
            int key = arr.get(i);  // The element to be inserted in the sorted part of the array
            int j = i - 1;  // The last element of the sorted part

            // Shift elements of the sorted part to the right until the correct position for key is found
            while (j >= 0 && arr.get(j) > key) {
                arr.set(j + 1, arr.get(j));  // Shift element to the right
                j--;  // Move to the next element on the left
            }

            arr.set(j + 1, key);  // Insert the key at its correct position

            printArray(arr);  // Print the array after each insertion
        }
    }
    
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

        Result.insertionSort2(n, arr);

        bufferedReader.close();
    }
}
