
public class InverseMatrix {

    /*
     * Finds the inverse using Dolytle
     */
    public static double[][] solve(double[][] A) {
        if (A.length != A[0].length) {
            return null;
        }
        int n = A.length;

        // Lii = 1
        double[][] L = new double[n][n], U = new double[n][n];
        for (int i = 0; i < n; i++) {
            L[i][i] = 1;
        }

        for (int k = 0; k < n; k++) {
            for (int j = k; j < n; j++) {
                double acum = 0;
                for (int p = 0; p <= k - 1; p++) {
                    acum += (L[k][p] * U[p][j]);
                }
                U[k][j] = A[k][j] - acum;
            }
            for (int i = k + 1; i < n; i++) {
                double acum = 0;
                for (int p = 0; p <= k - 1; p++) {
                    acum += (L[i][p] * U[p][k]);
                }
                L[i][k] = (A[i][k] - acum) / U[k][k];
            }
        }

        double[][] Ainv = new double[n][n];
        for (int i = 0; i < n; i++) {
            double[] b = new double[n], z = new double[n], x = new double[n];
            b[i] = 1;

            for (int j = 0; j < n; j++) {
                double acum = 0;
                for (int p = 0; p <= j - 1; p++) {
                    acum += (L[j][p] * z[p]);
                }
                z[j] = (b[j] - acum);
            }

            for (int j = n - 1; j >= 0; j--) {
                double acum = 0;
                for (int p = j + 1; p < n; p++) {
                    acum += (U[j][p] * x[p]);
                }
                x[j] = (z[j] - acum) / U[j][j];
            }

            for (int j = 0; j < n; j++) {
                Ainv[j][i] = x[j];
            }
        }
        return Ainv;
    }

}
