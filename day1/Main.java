/**
 * From Reddit
 */
package day1;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < 200; i++) {
            numbers.add(in.nextInt());
        }

        Collections.sort(numbers);
        for (int i = 0; i < 200; i++) {
            for (int j = i + 1; j < 200; j++) {
                int a = numbers.get(i);
                int b = numbers.get(j);
                int idx = Collections.binarySearch(numbers, 2020 - a - b);
                if (idx >= 0) {
                    System.out.println(a * b * numbers.get(idx));
                    return;
                }
            }
        }
    }
}