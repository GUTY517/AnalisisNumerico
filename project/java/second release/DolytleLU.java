
public class DolytleLU {

    public static double[] solucionar(double[][] A, double[] b) {
        if (A.length != A[0].length)
            return null;
        int n = A.length;

        // Lii = 1
        double[][] L = new double[n][n], U = new double[n][n];
        for (int i = 0; i < n; i++)
            L[i][i] = 1;

        for (int k = 0; k < n; k++) {
            for (int j = k; j < n; j++) {
                double acum = 0;
                for (int p = 0; p <= k - 1; p++)
                    acum += (L[k][p] * U[p][j]);
                U[k][j] = A[k][j] - acum;
            }
            for (int i = k + 1; i < n; i++) {
                double acum = 0;
                for (int p = 0; p <= k - 1; p++)
                    acum += (L[i][p] * U[p][k]);
                L[i][k] = (A[i][k] - acum) / U[k][k];
            }
        }

        double[] z = BasicMethods.progressiveSustitution(L, b);
        double[] x = BasicMethods.regresiveSustitution(U, z);
        
        return x;
    }

}
