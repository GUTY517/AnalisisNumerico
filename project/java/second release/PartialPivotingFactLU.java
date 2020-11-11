 


public class PartialPivotingFactLU {    

    public static double[] solve(double[][] A, double[] B) {
        
        int n = A.length;
        double[][] U = A, L = new double[n][n], P = new double[n][n];

        for (int i = 0; i < n; i++)

            P[i][i] = 1;

        for (int k = 0; k < n - 1; k++) {

            double great = 0;
            int pos_great = -1;

            for (int i = k; i < n; i++) {

                if (U[i][k] > great) {
                    great = U[i][k];
                    pos_great = i;
                }
            }
            if (great == 0) 

                return null;

            if (pos_great != k) {

                for (int i = 0; i < n; i++) {

                    double temp = U[k][i];
                    U[k][i] = U[pos_great][i];
                    U[pos_great][i] = temp;
                    temp = L[k][i];
                    L[k][i] = L[pos_great][i];
                    L[pos_great][i] = temp;
                    temp = P[k][i];
                    P[k][i] = P[pos_great][i];
                    P[pos_great][i] = temp;
                }
            }

            for (int i = k + 1; i < n; i++) {

                L[i][k] = U[i][k] / U[k][k];

                for (int j = k; j < n; j++) {
                    U[i][j] -= L[i][k]*U[k][j];
                }
            }
        }

        for (int i = 0; i < n; i++)

            L[i][i] = 1;

        B = Util.timesMatrix(P,B); 

        double[] Z = new double[n];

        for (int i = 0; i < n; i++) {

            double acum = 0;
            for (int p = 0; p < i; p++)
                acum += L[i][p]*Z[p];
            Z[i] = B[i] - acum;
        }

        double[] X = new double[n];

        for (int i = n - 1; i >= 0; i--) {

            double acum = 0;
            for (int p = i + 1; p < n; p++)
                acum += U[i][p]*X[p];
            X[i] = (Z[i] - acum) / U[i][i];
        }

        return X;
    }

}
