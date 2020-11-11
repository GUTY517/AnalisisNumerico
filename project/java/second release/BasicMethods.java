
/**
 * This class contains the basics methods to solve systems
 * <p>
 * Each method is declared as static to make it easy to acess from other classes
 * 
 */
public class BasicMethods {

    public static void printMatrix3D(double[][][] M) {
        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M[0].length; j++) {
                for (int k = 0; k < M[0][0].length; k++) {
                    System.out.print(M[i][j][k] + " ");
                }
                System.out.println();
            }
            System.out.println("\n-\n");
        }
    }

     public static void copyElements(double[][] A, double[][] B) {
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++)
                B[i][j] = A[i][j];
        }
    }

    public static double[] progressiveSubstitution(double[][] L, double[] b) {
        int n = L.length;
        double[] z = new double[n];
        for (int j = 0; j < n; j++) {
                double acum = 0;
                for (int p = 0; p <= j - 1; p++)
                    acum += (L[j][p] * z[p]);
                z[j] = (b[j] - acum);
        }
        return z;
    }

    public static double[] regresiveSubstitution(double[][] U, double[] z) {
        int n = U.length;
        double[] x = new double[n];
        for (int j = n - 1; j >= 0; j--) {
                double acum = 0;
                for (int p = j + 1; p < n; p++)
                    acum += (U[j][p] * x[p]);
                x[j] = (z[j] - acum) / U[j][j];
        }
        return x;
    }

    public static double[] regresiveSubstitution (double[][] A){
        int n = A.length;
        double[] X = new double[n];
        double acum;
        for (int i = n - 1; i >= 0; i--) {
            acum = 0;
            for (int p = i + 1; p < n; p++) {
                acum += A[i][p]*X[p];
            }
            X[i] = (A[i][n] - acum) / A[i][i];
        }
        return X;
    }

    public static double euclidianRule(double[] V) {
        double acum = 0;
        for (int i = 0; i < V.length; i++)
            acum += (V[i]*V[i]);
        return Math.sqrt(acum);
    }

    public static double rule(double[] V) {
        double mayor = 0;
        for (int i = 0; i < V.length; i++) {
            if (mayor < Math.abs(V[i]))
                mayor = Math.abs(V[i]);
        }
        return mayor;
    }

    public static double[] subVector(double[] V1, double[] V2) {
        if (V1.length != V2.length) return null;
        double[] Vr = new double[V1.length];
        for (int i = 0; i < V1.length; i++)
            Vr[i] = V1[i] - V2[i];
        return Vr;
    }

    public static double[][] gaussianElimination (double[][]A){
        double Mik = 0;
        int n = A.length;
        for (int k = 0; k<n - 1; k++){
            for (int i = k + 1; i < n; i++){
                Mik = A[i][k] / A[k][k];
                for (int j = k; j < n + 1; j++){
                    A[i][j] = A[i][j] - Mik * A[k][j];
                }
            }
        }

        return A;
    }

    public static double[][] extendedMatrix (double[][]A, double []B){
        int n = A.length;
        double[][] AA = new double[n][n + 1];
        for (int i = 0; i < n; i++) {
            int j = 0;
            for (j = 0; j < n; j++) {
                AA[i][j] = A[i][j];
            }
            AA[i][j] = B[i];
        }

        return AA;
    }

    public static double[][] LU_Method (double[][]A, double[][]U){
        int n = A.length;
        double[][]L = new double[n][n];
        for (int i = 0; i < n; i++){
            for (int j = 0; i < n; j++){
                if (i == j){
                    L[i][j] = 1;
                }
                else
                    if (i != j){
                        L[i][j] = 0;
                    }
            }
        }
        return L;
    }

    public static void printMatrix(double[][] A) {
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++)
                System.out.print(A[i][j] + " ");
            System.out.println();
        }
        System.out.println();
    }

    public static void printVector(double[] V) {
        for (int i = 0; i < V.length; i++)
            System.out.print(V[i] + " ");
        System.out.println("\n");
    }

    public static void main(String[] args) {
                double[][] test = {
            {30, -4, 6, -7, 1},
            {1, 76, -8, 4, -7},
            {2, -3, 56, -7, 8},
            {1, -6, 4, -78, 5},
            {3, -7, 8, -9, 116}
        };
        double[] B = {12,36,105,16,36};
        double[][]test2 = BasicMethods.extendedMatrix(test, B);
        double[]X = BasicMethods.regresiveSubstitution(test2);
        for (int i = 0; i< X.length; i++){
            System.out.println("X["+ i + "] = " + X[i]);
        }
    }
}