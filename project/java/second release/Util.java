
public class Util {

    public static void printMatrix(double[][] A) {
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++)
                System.out.print(A[i][j] + " ");
            System.out.println();
        }
    }

    public static double[][] timesMatrix(double[][] A, double[][] B) {
        if (A[0].length != B.length)
            return null;
        int x = A.length, y = B[0].length, n = A[0].length;
        double[][] R = new double[x][y];
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                double acum = 0;
                for (int k = 0; k < n; k++)
                    acum += A[i][k] * B[k][j];
                R[i][j] = acum;
            }
        }
        return R;
    }

    public static double[] timesMatrix(double[][] A, double[] B) {
        if (A[0].length != B.length)
            return null;
        int x = A.length, n = B.length;
        double[] R = new double[n];
        for (int i = 0; i < x; i++) {
            double acum = 0;
            for (int j = 0; j < n; j++)
                acum += A[i][j] * B[j];
            R[i] = acum;
        }
        return R;
    }

}
