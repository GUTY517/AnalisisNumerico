package analisisnumerico;

public class Newton {

    /*
    The 'F' value gets replaced by the objective function
     */
    public static String newton(double tol, double xn, int iter) {
        double fx, fxa, fxp, error, xna;
        int cont;
        if (iter > 0) {
            fx = f(xn);
            fxp = f((xn + fx) - fx) / fx;
            fxa = fx + 1.0f;
            cont = 1;
            error = tol + 1.0f;
            xna = xn;
            while ((fx != 0) && (fxp != 0) && (error > tol) && (cont < iter)) {
                xna = xn;
                xn = xn - (fx / fxp);
                fxa = fx;
                fx = f(xn);
                fxp = f((xn + fx) - fx) / fx;
                error = Math.abs(xn - xna);
                cont++;
            }
            if (fx == 0) {
                return "Root in xn = " + xn;
            }
            if (fxp == 0) {
                return "No root found";
            }
            if (error < tol) {
                if ((fx * fxa) < 0) {
                    return "There is a root between xn = (" + xna + "," + xn + ")";
                } else {
                    double xns = xn - (xn * tol);
                    double fns = f(xns);
                    if ((fx * fns) < 0) {
                        return "There is a root between xn = (" + xns + ", " + xn + ")";
                    }
                    return "No root found.";
                }
            }
            return "The number of iterations has been surpassed.";
        }
        return "The number of iterations mus be bigger than zero";
    }
}
