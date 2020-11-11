public class NewtonLU {

    private static double[] b;
    private static boolean[][] calculated;     
    private static double[][] previousCalc;    
    private static double[] x;
    private static double[] fx;

    public static double[] solve(double[] x, double[] fx) {
        int n = x.length;
        b = new double[n];
        calculated = new boolean[n][n];
        previousCalc = new double[n][n];
        NewtonLU.x = x;
        NewtonLU.fx = fx;
        b[0] = fx[0];
        difDiv(x.length-1, 0);
        return b;
    }

    public static double difDiv(int i, int k) {
        if (i == k) return fx[i];
        double f1 = 0;
        if (calculated[i-1][k]) {
            f1 = previousCalc[i-1][k];
        } else {
            f1 = difDiv(i-1, k);
        }
        double f2 = 0;
        if (calculated[i][k+1]) {
            f2 = previousCalc[i][k+1];
        } else {
            f2 = difDiv(i, k+1);
        }
        double dd = (f1 - f2) / (x[k] - x[i]);
        calculated[i][k] = true;
        previousCalc[i][k] = dd;
        if (k == 0)     
            b[i] = dd;
        return dd;
    }

    public static double calcValue(double x, double[] b, double[] xs) {
        double res = 0;
        for (int i = 0; i < b.length; i++) {
            double acum = b[i];
            for (int j = 0; j < i; j++)
                acum *=  (x - xs[j]);
            res += acum;
        }
        return res;
    }

}
