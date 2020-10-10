package analisisnumerico;

/**
 *
 * @author Yashua
 */
public class Newton {

    /*
    La 'F' se reemplaza con la funcion objetivo
     */
    public static String metodoNewton(double tol, double xn, int iter) {
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
                return "Raíz en xn = " + xn;
            }
            if (fxp == 0) {
                return "Yo creo que fallé :3";
            }
            if (error < tol) {
                if ((fx * fxa) < 0) {
                    return "Entre xn = (" + xna + "," + xn + ") existe una raíz.";
                } else {
                    double xns = xn - (xn * tol);
                    double fns = f(xns);
                    if ((fx * fns) < 0) {
                        return "Entre xn = (" + xns + ", " + xn + ") existe una raíz.";
                    }
                    return "Falló en encontrar una raíz.";
                }
            }
            return "Superado el número de iteraciones.";
        }
        return "El número de iteraciones debe ser mayor a 0.";
    }
}
