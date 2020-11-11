public class JacobiLU {

    private static double[][] A;
    private static double[] b;

    public static double[] solve(double[][] A, double[] b, double[] V, double lambda, double tol, int iter) {
        JacobiLU.A = A;
        JacobiLU.b = b;
        int n = V.length;
        int cont = 0;
        double err = tol + 1;
        while (err > tol && cont <= iter) {
            BasicMethods.printVector(V);
            double[] N = new double[n];
            for (int i = 0; i < n; i++)
                N[i] = g(V, i, lambda);
            err = Math.abs(BasicMethods.rule(N) - BasicMethods.rule(V));
            cont++;
            V = N.clone();
        }
        if (err <= tol)
            return V;
        else
            return null;
    }

    public static double g(double[] V, int i, double lambda) {
        double sum1 = 0;
        for (int p = 0; p < i; p++)
            sum1 += A[i][p] * V[p];
        double sum2 = 0;
        for (int q = i + 1; q < V.length; q++)
            sum2 += A[i][q] * V[q];
        double x = (b[i] - sum1 - sum2) / A[i][i];
        x = lambda * x + (1 - lambda) * V[i];
        return x;
    }

    public static void main(String[] args) {
        double [][]test = {
                    {5,-12,-1},
                    {-3,7,-16},
                    {-17,-2,8}};

        double [] testB = {43,56,38};

        double[]V = {0,0,0};

        double tol = 0.001d;

        int iter = 20;

        double[]X = new double[3];
               X = JacobiLU.solve(test, testB, V, 1, tol, iter);

        System.out.println("Result");
        BasicMethods.printVector(X);
    }

}
