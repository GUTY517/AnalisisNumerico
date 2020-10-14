
package analisisnumerico;

public class Secante {

    /*
    'F'  gets replaced by the objective function
     */
    public static String secant(double tol, double x0, double x1, int iter) {
        double fx0, fx1, error, x1a;
        int cont;
        if (iter > 0) {
            fx0 = f(x0);
            fx1 = f(x1);
            cont = 1;
            error = tol + 1;
            while ((fx1 != 0) && (error > tol) && (cont < iter)) {
                x1a = x1;
                x1 = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0));
                x0 = x1a;
                fx0 = fx1;
                fx1 = f(x1);
                error = Math.abs(x1 - x0);
                cont++;
            }
            if (fx1 == 0) {
                return "Root found in xn = " + x1;
            }
            if (error < tol) {
                if ((fx1 * fx0) < 0) {
                    return "There is a root between xn = (" + x0 + "," + x1 + ")";
                } else {
                    double xns = x1 - (x1 * tol);
                    double fns = f(xns);
                    if ((fx1 * fns) < 0) {
                        return "There is a root between xn = (" + xns + ", " + x1 + ")";
                    }
                    return "No root found.";
                }
            }
            return "The number of iterations has been surpassed.";
        }
        return "The number of iterations mus be bigger than zero";
    }
}
