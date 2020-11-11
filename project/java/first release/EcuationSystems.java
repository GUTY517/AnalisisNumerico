/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package analisisnumerico;

/**
 *
 * @author Yashua
 */
public class EcuationSystems {

    public static double[][] Gauss(double[][] a) {
        int n = a.length;
        for (int k = 0; k < n - 1; k++) {
            for (int i = k + 1; i < n; i++) {
                double mult = a[i][k] / a[k][k];
                for (int j = k; j < n + 1; j++) {
                    a[i][j] = a[i][j] - mult * a[k][j];
                }
            }
        }
        return a;
    }

    public static double[] RegresiveSubstitution(double[][] ab) {
        int n = ab.length;
        double[] x = new double[n];
        x[n - 1] = ab[n - 1][n] / ab[n - 1][n - 1];
        for (int i = n - 1; i >= 0; i--) {
            double cont = 0;
            for (int j = i + 1; j < n; j++) {
                cont += (ab[i][j] * x[j]);
            }
            x[i] = (ab[i][n] - cont) / ab[i][i];
        }
        return x;
    }

    public static double[][] PartialPivoting(double[][] a, int k) {
        double great = Math.abs(a[k][k]);
        int fGreat = k;
        int n = a.length;
        for (int i = k + 1; i < n; i++) {
            if (Math.abs(a[i][k]) > great) {
                great = a[i][k];
                fGreat = i;
            }
        }
        if (great == 0) {
            System.out.println("The system doesn't have unic answer");
        } else if (fGreat != k) {
            swapRows(a, fGreat, k);
        }
        return a;
    }

    public static double[][] TotalPivoting(double[][] a, int k) {
        double great = 0;
        int rowgreat = k;
        int columngreat = k;
        int n = a.length;
        int[] marks = new int[n];

        for (int i = 1; i <= n; i++) {
            marks[i - 1] = i;
        }
        for (int i = k; i < n; i++) {
            for (int j = k; j < n; j++) {
                if (Math.abs(a[i][j]) > great) {
                    great = Math.abs(a[i][j]);
                    rowgreat = i;
                    columngreat = j;
                }
            }
        }
        if (great == 0) {
            System.out.println("The system doesn't have an unic answer");
        } else {
            if (rowgreat != k) {
                a = swapRows(a, rowgreat, k);
            }
            if (columngreat != k) {
                a = swapCol(a, columngreat, k);
                int temp = marks[columngreat];
                marks[columngreat] = marks[k];
                marks[k] = temp;
            }
        }
        return a;
    }

    public static double[][] swapCol(double a[][], int columngreat, int k) {
        for (int i = 1; i <= columngreat; i++) {
            double aux = a[i][1];
            a[i][1] = a[i][k];
            a[i][k] = aux;
        }
        return a;
    }
     public static double[][] swapRows(double a[][], int fGreat, int k) {
        for (int i = 1; i <= fGreat; i++) {
            double aux = a[i][1];
            a[i][1] = a[k][i];
            a[i][k] = aux;
        }
        return a;
    }

}
