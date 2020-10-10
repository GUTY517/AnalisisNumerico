
package analisisnumerico;

/**
 *
 * @author Yashua
 */
public class Secante {

    /*
    La 'F'  se reemplaza con la funcion objetivo
     */
    public static String metodoSecante(double tol, double x0, double x1, int iter) {
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
                return "Raíz en xn = " + x1;
            }
            if (error < tol) {
                if ((fx1 * fx0) < 0) {
                    return "Entre xn = (" + x0 + "," + x1 + ") existe una raíz.";
                } else {
                    double xns = x1 - (x1 * tol);
                    double fns = f(xns);
                    if ((fx1 * fns) < 0) {
                        return "Entre xn = (" + xns + ", " + x1 + ") existe una raíz.";
                    }
                    return "Falló en encontrar una raíz.";
                }
            }
            return "Superado el número de iteraciones.";
        }
        return "El número de iteraciones debe ser mayor a 0.";
    }
}
