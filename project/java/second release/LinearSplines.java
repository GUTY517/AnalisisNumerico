public class LinearSplines {

    private static Ecuation[] splines;
    
    private static class Ecuation {
        private double lowerLimit, upperLimit, a, b;
        public Ecuation(double a1, double b1, double ll, double lu) {
            lowerLimit = ll;
            upperLimit = lu;
            a = a1;
            b = b1;
        }
        public double getLimInf() { return lowerLimit; }
        public double getLimSup() { return upperLimit; }
        public double getA() { return a; }
        public double getB() { return b; }
    }

    public static Ecuation[] solve(double[] xs, double[] ys) {
        int n = xs.length;
        splines = new Ecuation[n-1];

        for (int i = 0; i < n-1; i++) {
            double m = (ys[i+1] - ys[i]) / (xs[i+1] - xs[i]);
            double b = ys[i] - xs[i] * m;
            splines[i] = new Ecuation(m, b, xs[i], xs[i+1]);
        }

        return splines;
    }

}
