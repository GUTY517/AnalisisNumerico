import java.util.Scanner;

public class falseRule {
 
    /**
     * ℯ^((3x-12))+x*cos(3x)-x^(2)+4 interval [2,3]
     *
     * @param xi Limite Inferior
     * @param xs Limite Superior
     * @param tol Tolerancia
     * @param ite Numero de Iteraciones
     */
    public void falseRule(double xi, double xs, double tol, int iter) {
        falseRule rf = new falseRule();
        double yi = rf.Fx(xi);
        double ys = rf.Fx(xi);

        if (yi == 0) {
            System.out.println("xi, is the bottom limit of the root");

        } else if (ys == 0) {
            System.out.println("xs, is the top limit of the root");

        } else {

            if (yi * ys < 0) {
                double xm = xi - (yi * (xs - xi)) / (ys - yi);
                double ym = rf.Fx(xm);

                int cont = 1;
                double error = tol + 1;

                while ((ym != 0) && (error > tol) && (cont < iter)) {

                    if (yi * ym < 0) {
                        xs = xm;
                        ys = ym;

                    } else {
                        xi = xm;
                        yi = ym;
                    }

                    double temp = xm;
                    xm = xi - (yi * (xs - xi)) / (ys - yi);
                    ym = rf.Fx(xm);

                    error = Math.abs(xm - temp);
                    cont = cont + 1;
                }

                if (ym == 0) {
                    System.out.println("xm is root, xm = " + xm);
                } else if (error < tol) {
                    System.out.println("xm is an aproximation of a root, with tolerance of: " + tol);
                    System.out.println("xm = " + xm);
                } else {
                    System.out.println("Failed in " + iter + " iterations");
                }

            } else {
                System.out.println("There is no sing change in the interval");
            }
        }
    }

    public Double Fx(double y) {
        y = Math.pow(Math.E, (3 * y) - 12) + y * Math.cos(3 * y) - Math.pow(y, 2) + 4;

        return y;
    }

    public static void main(String[] args) {

        Scanner reader = new Scanner(System.in);

        double xi = 0f, xs = 0f;
        double tol = 0f;
        int ite = 0;

        xi = reader.nextDouble();
        xs = reader.nextDouble();
        tol = reader.nextDouble();
        ite = reader.nextInt();

    }

}