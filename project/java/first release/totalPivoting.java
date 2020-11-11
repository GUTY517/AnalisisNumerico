    public static double[][] TotalPivoting(double[][] a, int k) { 
        double great = 0;
        int rowgreat = k;
        int columngreat = k;
        int n = a.length;
        int[] marks = new int[n];

        for (int i = 1; i <= n; i++) {
            marks[i - 1] = i;
        }
        for (int i = k; i < n; i++) {
            for (int j = k; j < n; j++) {
                if (Math.abs(a[i][j]) > great) {
                    great = Math.abs(a[i][j]);
                    rowgreat = i;
                    columngreat = j;
                }
            }
        }
        if (great == 0) {
            System.out.println("The system doesn't have an unic answer");
        } else {
            if (rowgreat != k) {
                a = swapRows(a, rowgreat, k);
            }
            if (columngreat != k) {
                a = swapCol(a, columngreat, k);
                int temp = marks[columngreat];
                marks[columngreat] = marks[k];
                marks[k] = temp;
            }
        }
        return a;
    }