import java.util.Scanner;

public class FractionalKnapsack {

    private static double getOptimalValue(int capacity, int[] values, int[] weights) {
        double value = 0;
        double[] vw = new double[values.length];
        int bigi = 0;
        for (int i = 0; i < values.length; i++) {
            vw[i] = (double)values[i]/weights[i];
            if (vw[i] > vw[bigi]) bigi = i;
        }
        while (capacity > 0) {
            if (capacity > weights[bigi]) {
                capacity -= weights[bigi];
                value += values[bigi];
                vw[bigi] = 0;
                bigi = 0;
                for (int i = 0; i < vw.length; i++) {
                    if (vw[i] > vw[bigi]) bigi = i;
                }
            }
            else {
                value += values[bigi] * ((double)capacity/weights[bigi]);
                capacity = 0;
            }
        }

        //write your code here

        return value;
    }


    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int capacity = scanner.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
            weights[i] = scanner.nextInt();
        }
        System.out.printf("%.4f", getOptimalValue(capacity, values, weights));
    }
} 
