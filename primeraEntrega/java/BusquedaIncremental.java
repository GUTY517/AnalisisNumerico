

/**
 *
 * @author Yashua
 */
import java.util.Scanner;
public class BusquedaIncremental {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Inserte los valores de: X0, iteraciones y Delta");
        busqueda();
    }

    public static void busqueda() {
        Scanner lector = new Scanner(System.in);
        double x0 = lector.nextInt();
        double ite = lector.nextInt();
        double delta = lector.nextInt();

        double y0 = funcion(x0);

        if (y0 == 0) {
            System.out.println("El valor: " + x0 + ", es una raíz.");
            System.exit(0);
        } else if (delta == 0) {
            System.out.println("El valor de delta es inapropiado.");
            System.exit(0);
        } else if (ite <= 0) {
            System.out.println("El valor de las iteraciones es inapropiado.");
            System.exit(0);
        } else {
            
            double x1 = x0 + delta;
            double y1 = funcion(x1);
            int cont = 1;

            while ((y0 * y1) > 0 && (cont < ite)) {
                
                x0 = x1;
                y0 = y1;
                x1 = x1 + delta;
                y1 = funcion(x1);
                System.out.println("valor de y0 = "+y0+ ", valor y1 = "+y1);
                cont++;
            }
            if ((y1 * y0) < 0) {
                System.out.println("Los valores de: [" + x0 + "], [" + x1 + "] definen un intervalo");
                System.exit(0);
            } else if (y1 == 0) {
                System.out.println("El valor de: " + x1 + " es una raíz");
                System.exit(0);
            } else {
                System.out.println("No se encontró ninguna raíz");
                System.exit(0);
            }
        }
    }

    public static double funcion(double x) {
        double e = Math.E;
        
        double resultado = Math.pow(e, ( (3*x) -12));
        resultado = resultado + (x* Math.cos(3*x)) - Math.pow(x, 2) +4;
        return resultado;
    }
}
