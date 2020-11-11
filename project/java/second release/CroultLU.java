
public class CroultLU {

    public static double[] solve(double[][] A, double[] b) {
        int n = A.length;
        double[][] U = new double[n][n], L = new double[n][n];
        for (int i = 0; i < n; i++)
            U[i][i] = 1;
        for (int k = 0; k < n; k++) {
            for (int i = k; i < n; i++) {
                double acum = 0;
                for (int p = 0; p < k; p++)
                    acum += (L[i][p] * U[p][k]);
                L[i][k] = A[i][k] - acum;
            }
            for (int j = k + 1; j < n; j++) {
                double acum = 0;
                for (int p = 0; p < k; p++)
                    acum += (L[k][p] * U[p][j]);
                U[k][j] = (A[k][j] - acum) / L[k][k];
            }
        }
        
        BasicMethods.printMatrix(U);
        BasicMethods.printMatrix(L);

        double[] z = BasicMethods.progressiveSubstitution(L, b);
        double[] x = BasicMethods.regresiveSubstitution(U, z);

        return x;

    }

}
