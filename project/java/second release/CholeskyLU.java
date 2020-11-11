
public class CholeskyLU {

    public static double[] solve(double[][] A, double[] b) {
        int n = A.length;
        double[][] L = new double[n][n], U = new double[n][n];
        for (int k = 0; k < n; k++) {
            BasicMethods.printMatrix(L);
            double acum = 0;
            for (int p = 0; p < k; p++)
                acum += L[k][p] * U[p][k];
            U[k][k] = Math.sqrt(A[k][k] - acum);
            L[k][k] = U[k][k];
            for (int i = k + 1; i < n; i++) {
                acum = 0;
                for (int p = 0; p < k; p++)
                    acum += L[i][p] * U[p][k];
                L[i][k] = (A[i][k] - acum) / U[k][k];
            }
            for (int j = k + 1; j < n; j++) {
                acum = 0;
                for (int p = 0; p < k; p++)
                    acum += L[k][p] * U[p][j];
                U[k][j] = (A[k][j] - acum) / U[k][k];
            }
        }
        BasicMethods.printMatrix(L);

        double[] z = BasicMethods.progressiveSubstitution(L, b);
        double[] x = BasicMethods.regresiveSubstitution(U, z);

        return x;
    }
}
