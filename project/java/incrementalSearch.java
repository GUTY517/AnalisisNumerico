import java.util.Scanner;
public class searchIncremental {

    public static void main(String[] args) {
        System.out.println("Input X0 values, iterations and delta");
        search();
    }

    public static void search() {
        Scanner reader = new Scanner(System.in);
        double x0 = reader.nextInt();
        double ite = reader.nextInt();
        double delta = reader.nextInt();

        double y0 = function(x0);

        if (y0 == 0) {
            System.out.println(x0 + " is a root.");
            System.exit(0);
        } else if (delta == 0) {
            System.out.println("Delta value is not correct.");
            System.exit(0);
        } else if (ite <= 0) {
            System.out.println("Itearions value is incorrect.");
            System.exit(0);
        } else {

            double x1 = x0 + delta;
            double y1 = function(x1);
            int cont = 1;

            while ((y0 * y1) > 0 && (cont < ite)) {

                x0 = x1;
                y0 = y1;
                x1 = x1 + delta;
                y1 = function(x1);
                System.out.println("y0 value = "+y0+ ", y1 value = "+y1);
                cont++;
            }
            if ((y1 * y0) < 0) {
                System.out.println("The values of: [" + x0 + "], [" + x1 + "] makes an interval");
                System.exit(0);
            } else if (y1 == 0) {
                System.out.println("The value of: " + x1 + " is a root");
                System.exit(0);
            } else {
                System.out.println("No root found");
                System.exit(0);
            }
        }
    }

    public static double function(double x) {
        double e = Math.E;

        double result = Math.pow(e, ( (3*x) -12));
        result = result + (x* Math.cos(3*x)) - Math.pow(x, 2) +4;
        return result;
    }
}
