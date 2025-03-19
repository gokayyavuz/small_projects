package JavaPractice;

import java.util.Arrays;

public class bubblesort {
    public static void main(String[] args) {
        int [] arr = {6,4,5,3,2,1};
        print(Arrays.toString(arr));
        for (int i = 0; i < arr.length - 1; i++) {
            print(Integer.toString(arr[i]));
            for (int j = 1; j < arr.length - 1 - i; j++) {
                if (arr[i] < arr[j]) {

                    int tmp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = tmp;
                    j++;
                    print(Arrays.toString(arr));
                }
            }
        }
        print(Arrays.toString(arr));
        
    }
    public static void print(String s) {
        System.out.println(s);
    }
}
