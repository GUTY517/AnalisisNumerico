

public class bisectionMethod { 
    /*
    'F' gets replaced with the objective function
    */

    public static String bisectionMethod(double xi, double xs, double tol, int iter)
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
                    if (ym == 0) return "The ecuation have a solution in xm = " + xm;
                    if (err < tol) return "There is an aproximate solution in xm = " + xm
			+ " with and absolut error of " + err;
			return "The number of iterations has been surpassed";
                    } else {
			return "The number of iterations mus be bigger than zero";
                    }
		}
            if (yi == 0) return "There is a root in xi = " + xi;
            if (ys == 0) return "There is a root in xs = " + xs;
            return "There is no root in the given interval.";
	}
}
