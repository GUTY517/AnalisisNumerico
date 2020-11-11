

public class GaussianaPivTotalLU {

    public static double[][] P;

    public static double[][][] solve(double[][] A, double[] B) {
        int n = A.length;
        double AA[][][] = new double[n-1][n][n+1];
        A = BasicMethods.extendedMatrix(A, B);
        P = new double[n][n];
        for (int i = 0; i < n; i++)
            P[i][i] = 1;

        for (int k = 0; k < n - 1; k++) {
            double great = 0;
            int rowPos = -1, columnPos = -1;
            for (int i = k; i < n; i++) {
                for (int j = k; j < n; j++) {
                    if (Math.abs(A[i][j]) > great) {
                        great = Math.abs(A[i][j]);
                        rowPos = i;
                        columnPos = j;
                    }
                }
            }
            if (great == 0) return null;
            if (k != rowPos) {
                for (int j = 0; j < n+1; j++) {
                   double temp = A[rowPos][j];
                   A[rowPos][j] = A[k][j];
                   A[k][j] = temp;
                }
            }
            if (k != columnPos) {
                for (int i = 0; i < n; i++) {
                    double temp = A[i][columnPos];
                    A[i][columnPos] = A[i][k];
                    A[i][k] = temp;
                    temp = P[i][columnPos];
                    P[i][columnPos] = P[i][k];
                    P[i][k] = temp;
                }
            }
            for (int i = k + 1; i < n; i++) {
                double m = A[i][k] / A[k][k];
                for (int j = k; j < n+1; j++) {
                    A[i][j] = A[i][j] - m * A[k][j];
                }
            }
            BasicMethods.copyElements(A, AA[k]);
        }
        return AA;
    }

    public static double[] getResults(double[][] A) {
        double[] X = BasicMethods.regresiveSustitution(A);
        X = Util.timesMatrix(P, X);
        return X;
    }
    

}
