package analisisnumerico;

import java.util.Scanner;
import java.util.StringTokenizer;

public class DecABin {

    public static void main(String[] args) {

        int exp, digito;
        int[] entDec = new int[2];
        double bin;
        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce un numero");
        String numer = sc.nextLine();
        StringTokenizer tokens = new StringTokenizer(numer, ".");

        int cont = 0;
        while (tokens.hasMoreTokens()) {
            String str = tokens.nextToken();
            entDec[cont] = Integer.parseInt(str);
            cont++;
        }

        exp = 0;
        bin = 0;
        while (entDec[0] != 0) {
            digito = entDec[0] % 2;
            bin = bin + digito * Math.pow(10, exp);
            exp++;
            entDec[0] = entDec[0] / 2;
        }
        
        float digitF = 0;
        digitF = entDec[1];
        cont = 0;

        String decFlot = ".";

        digitF = digitF / 10;
        while (digitF != 0 && cont < 6) {
            digitF = digitF * 2;

            if (digitF > 1) {
                decFlot += "1";
                digitF = digitF - 1;
            } else {
                decFlot += "0";
            }
            cont++;
        }
        System.out.printf("bin: %.0f", bin);
        System.out.println(decFlot);
    }
}