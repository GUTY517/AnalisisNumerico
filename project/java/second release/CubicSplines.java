
public class CubicSplines {

    private static double[][] splines;

    public static void spline(double x, double y, int i, int ec) {
        for (int exp = 3, j = ec * 4; exp >= 0; exp--, j++) {
            splines[i][j] = Math.pow(x, exp);
            splines[i+1][j+4] = Math.pow(x, exp);
        }
        splines[i][splines[i].length-1] = y;
        splines[i+1][splines[i].length-1] = y;
    }

    public static void extremeSpline(double x, double y, int i, boolean first) {
        if (first) {
            for (int exp = 3, j = 0; exp >= 0; exp--, j++) {
                splines[i][j] = Math.pow(x, exp);
            }
            splines[i][splines[i].length - 1] = y;
        } else {
            for (int exp = 3, j = splines[i].length - 5; exp >= 0; exp--, j++) {
                splines[i][j] = Math.pow(x, exp);
            }
            splines[i][splines[i].length - 1] = y;
            
        }
    }

    public static void firstDerivateSpline(double x, double y, int i, int ec) {
        for (int exp = 2, j = ec * 4; exp >= 0; exp--, j++) {
            splines[i][j] = (exp + 1) * Math.pow(x, exp);
            splines[i][j + 4] = - (exp + 1) * Math.pow(x, exp);
        }
    }

    public static void secondDerivateSpline(double x, double y, int i, int ec) {
        int j = ec * 4;
        splines[i][j] = 6 * x;
        splines[i][j + 1] = 2;
        splines[i][j + 4] = -6 * x;
        splines[i][j + 5] = -2;
    }

    public static void extremeSplineSecondDerivate(double x, double y, int i, boolean first) {
        if (first) {
            splines[i][0] = 6 * x;
            splines[i][1] = 2;
        } else {
            splines[i][splines[i].length - 5] = 6 * x;
            splines[i][splines[i].length - 4] = 2;
        }
    }

    public static double[][] solve(double[] xs, double[] ys) {
        int n = xs.length;
        splines = new double[4*(n-1)][4*(n-1) + 1];
        int ec = 1, i = 0;
        while (ec < n-1) {
            spline(xs[ec], ys[ec], i, ec-1);
            i += 2;
            ec++;
        }
        extremeSpline(xs[0], ys[0], i++, true);
        extremeSpline(xs[n-1], ys[n-1], i++, false);
        ec = 1;
        while (ec < n-1) {
            firstDerivateSpline(xs[ec], ys[ec], i, ec-1);
            i++;
            ec++;
        }
        ec = 1;
        while (ec < n-1) {
            secondDerivateSpline(xs[ec], ys[ec], i, ec-1);
            ec++;
            i++;
        }
        extremeSplineSecondDerivate(xs[0], ys[0], i++, true);
        extremeSplineSecondDerivate(xs[n-1], ys[n-1], i++, false);
        return splines;
    }
}
