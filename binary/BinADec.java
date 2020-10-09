package analisisnumerico;

import java.util.Scanner;
import java.util.StringTokenizer;

public class BinADec {

    public static void main(String[] args) {

        String[] arr = new String[2];

        Scanner sc = new Scanner(System.in);

        System.out.println("Insert a binary number to cast in float");
        String numer = sc.nextLine();
        StringTokenizer tokens = new StringTokenizer(numer, ".");

        int cont = 0;
        while (tokens.hasMoreTokens()) {
            String str = tokens.nextToken();
            arr[cont] = str;
            cont++;
        }

        double parteEntera = 0;

        String strInt = arr[0];
        int tam = arr[0].length();
        int exp = tam - 1;

        for (int i = 0; i < tam; i++) {
            if (strInt.charAt(i) == '1') {
                parteEntera += Math.pow(2, exp);
            }
            exp--;
        }

        if (cont > 1) {
            exp = 1;
            double consIni = 0.5;
            strInt = arr[1];
            for (int i = 0; i < arr[1].length(); i++) {
                if (strInt.charAt(i) == '1') {

                    parteEntera += 1 * consIni;

                }
                consIni = consIni * 0.5;
                exp++;
            }
            System.out.println(parteEntera);
        } else {
            System.out.println(parteEntera);
        }
    }
}
