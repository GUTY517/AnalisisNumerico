   public static double[][] swapCol(double a[][], int columngreat, int k) { 
        for (int i = 1; i <= columngreat; i++) {
            double aux = a[i][1];
            a[i][1] = a[i][k];
            a[i][k] = aux;
        }
        return a;
    }
     public static double[][] swapRows(double a[][], int fGreat, int k) {
        for (int i = 1; i <= fGreat; i++) {
            double aux = a[i][1];
            a[i][1] = a[k][i];
            a[i][k] = aux;
        }
        return a;
    }