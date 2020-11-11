
public class Raices {

    /*
    The 'F', 'fp', 'fpp' get replaced by the objective function
     */
    public static String multipleRoots(double tol, double xn, int iter) {
        double fx, fxpp, fxp, error, xna, fxa;
        int cont;
        if (iter > 0) {
            fx = f(xn);
            fxp = fp(xn);
            fxpp = fpp(xn);
            fxa = fx;
            xna = xn;
            cont = 1;
            error = tol + 1.0f;

            while ((fx != 0) && (error > tol) && (cont < iter)) {
                xna = xn;
                xn = xn - (fx * fxp) / (fxp * fxp - fx * fxpp);
                fxa = fx;
                fx = f(xn);
                fxp = fp(xn);
                fxpp = fpp(xn);
                error = Math.abs(xn - xna);
                cont++;
            }
            System.out.println(xn);
            if (fx == 0) {
                return "Root found in xn = " + xn;
            }
            if (error < tol) {
                if ((fx * fxa) < 0) {
                    return "There is a root between xn = (" + xna + "," + xn + ")";
                } else {
                    double xns = xn - xna;
                    double fns = fp(xn + xns);
                    if ((fxp * fns) < 0) {
                        return xn + " is an aproximate root";
                    }
                    return "No root found.";
                }
            }
            return "The number of iterations has been surpassed.";
        }
        return "The number of iterations mus be bigger than zero";
    }
}
