import java.util.Scanner;

/**
 *
 * @author Yashua
 */
public class ReglaFalsa {

    /**
     * ℯ^((3x-12))+x*cos(3x)-x^(2)+4 intervalo [2,3]
     *
     * @param xi Limite Inferior
     * @param xs Limite Superior
     * @param tol Tolerancia
     * @param ite Numero de Iteraciones
     */
    public void reglaFalsa(double xi, double xs, double tol, int iter) {
        ReglaFalsa rf = new ReglaFalsa();
        double yi = rf.Fx(xi);
        double ys = rf.Fx(xi);

        if (yi == 0) {
            System.out.println("xi, el limite inferior es raiz");

        } else if (ys == 0) {
            System.out.println("xs, el limite superior es raiz");

        } else {

            if (yi * ys < 0) {
                double xm = xi - (yi * (xs - xi)) / (ys - yi);
                double ym = rf.Fx(xm);

                int contador = 1;
                double error = tol + 1;

                while ((ym != 0) && (error > tol) && (contador < iter)) {

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
                    contador = contador + 1;
                }

                if (ym == 0) {
                    System.out.println("El valor de xm es raiz, xm = " + xm);
                } else if (error < tol) {
                    System.out.println("El valor de xm es una aproximacion a la raiz, con tolerancia de: " + tol);
                    System.out.println("Valor de xm = " + xm);
                } else {
                    System.out.println("Fracaso en " + iter + " iteraciones");
                }

            } else {
                System.out.println("Intervalo inadecuado no hay cambio de signo");
            }
        }
    }

    public Double Fx(double y) {
        y = Math.pow(Math.E, (3 * y) - 12) + y * Math.cos(3 * y) - Math.pow(y, 2) + 4;

        return y;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        Scanner lector = new Scanner(System.in);

        double xi = 0f, xs = 0f;
        double tol = 0f;
        int ite = 0;

        xi = lector.nextDouble();
        xs = lector.nextDouble();
        tol = lector.nextDouble();
        ite = lector.nextInt();

    }

}