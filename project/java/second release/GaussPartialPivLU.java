
public class GaussPartialPivLU {

    public static double[][][] solve(double[][] A, double[] b) {
        int n = A.length;
        double[][][] AA = new double[n-1][n][n+1];
        A = BasicMethods.extendedMatrix(A, b);
        for (int k = 0; k < n - 1; k++) {
            double great = 0;
            int posGreat = -1;
            for (int i = k; i < n; i++) {
                if (Math.abs(A[i][k]) > great) {
                    great = Math.abs(A[i][k]);
                    posGreat = i;
                }
            }
            if (great == 0) {
                return null;
            }

            if (k != posGreat) {
                double temp;
                for (int i = 0; i < n+1; i++) {
                    temp = A[posGreat][i];
                    A[posGreat][i] = A[k][i];
                    A[k][i] = temp;
                }
            }

            double Mik = -1;
            for (int i = k + 1; i < n; i++){
                Mik = A[i][k] / A[k][k];
                for (int j = k; j < n + 1; j++){
                    A[i][j] = A[i][j] - (Mik * A[k][j]);
                } //j
            }//i
            int h = k + 1;
            System.out.println("step " + String.valueOf(h));
            BasicMethods.copyElements(A, AA[k]);
        }// k
        return AA;
    }

    public double[] getResult(double[][] A) {
        double[] X = BasicMethods.regresiveSustitution(A);
        return X;
    }

}