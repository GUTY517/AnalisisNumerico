
package analisisnumerico;

/**
 *
 * @author Yashua
 */
public class bisectionMethod {
    /*
    La 'F' se reemplaza con la funcion objetivo
    */
    
    public static String metodoBiseccion(double xi, double xs, double tol, int iter)
	{	
            double xm, yi, ys, ym, err = 5.0f, erra;
            int cont;
            yi = f(xi);
            ys = f(xs);
            if ((yi * ys) < 0) {
                if (iter > 0) {
                    xm = (xi + xs) / 2;
                    ym = f(xm);
                    erra = xm;
                    cont = 1;
                    while ((ym != 0) && (err > tol) && (cont < iter)) {
                        if ((yi * ym) < 0) {
                            xs = xm;
                            ys = ym;
                        } else {
                            xi = xm;
                            yi = ym;
                        }
                        xm = (xi + xs) / 2;
                        ym = f(xm);
                        err = Math.abs(xm - erra);
                        erra = xm;
                        cont++;
                    }
                    if (ym == 0) return "La ecuación tiene solución en xm = " + xm;
                    if (err < tol) return "La ecuación tiene solución aproximada en xm = " + xm 
			+ " con un error absoluto de " + err;
			return "El número de iteraciones ha sido superado.";
                    } else {
			return "El número de iteraciones debe ser mayor a 0.";
                    }
		}
            if (yi == 0) return "En xi = " + xi + " existe una raíz.";
            if (ys == 0) return "En xs = " + xs + " existe una raíz.";
            return "Dentro del intervalo dado no se encuentra una raíz.";
	}
}
