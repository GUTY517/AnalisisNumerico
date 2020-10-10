package analisisnumerico;

/**
 *
 * @author Yashua
 */
public class Raices {

    /*
    La 'F', 'fp', 'fpp' se reemplaza con la funcion objetivo
     */
    public static String raicesMultiples(double tol, double xn, int iter) {
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
                return "Raíz en xn = " + xn;
            }
            if (error < tol) {
                if ((fx * fxa) < 0) {
                    return "Entre xn = (" + xna + "," + xn + ") existe una raíz.";
                } else {
                    double xns = xn - xna;
                    double fns = fp(xn + xns);
                    if ((fxp * fns) < 0) {
                        return xn + " es una aproximacion a una raiz";
                    }
                    return "Falló en encontrar una raíz.";
                }
            }
            return "Superado el número de iteraciones.";
        }
        return "El número de iteraciones debe ser mayor a 0.";
    }
}
