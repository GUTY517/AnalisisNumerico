
package analisisnumerico;

/**
 *
 * @author Yashua
 */
public class PuntoFijo {

    /*
    La 'F' y 'g' se reemplaza con la funcion objetivo
     */
    public static String metodoPuntoFijo(double tol, double xn, int iter) {
        double fx, fxa, error, xna;
        int cont;
        if (iter > 0) {
            fx = f(xn);
            fxa = fx + 1.0f;
            cont = 1;
            error = tol + 1.0f;
            xna = xn;
            while ((fx != 0) && (error > tol) && (cont < iter)) {
                xna = xn;
                xn = g(xn);
                fxa = fx;
                fx = f(xn);
                error = Math.abs(xn - xna);
                cont++;
            }
            if (fx == 0) {
                return "Raíz en xn = " + xn;
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
