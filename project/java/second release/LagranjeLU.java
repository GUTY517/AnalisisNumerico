
public class LagranjeLU {


    public static double solve(Polynomial[] L, double[] fx, double x) {
        double acum = 0;
        int n = fx.length;
        for (int i = 0; i < n; i++) {
            acum += (L[i].evaluate(x) * fx[i]);
        }
        return acum;
    }

    public static Polynomial[] getCoeficients(double[] xs) {
        int n = xs.length;
        Polynomial[] L = new Polynomial[n];
        for (int i = 0; i < n; i++) {
            double denom = 1;
            L[i] = new Polynomial();
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    double[] co = {-xs[j], 1};
                    L[i] = L[i].times(new Polynomial(co));
                    denom *= (xs[i] - xs[j]);
                }
            }
            L[i] = L[i].divide(denom);
        }
        return L;
    }

}
