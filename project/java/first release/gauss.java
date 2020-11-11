public static double[][] Gauss(double[][] a) { 
      int n = a.length;
      for (int k = 0; k < n - 1; k++)
      {
        for (int i = k + 1; i < n; i++)
        {
          double mult = a[i][k]/a[k][k];
          for (int j = k; j < n + 1; j++)
          {
            a[i][j] = a[i][j] - mult*a[k][j];
          }
        }
      }
      return a;
    }

    public static double[] RegresiveSubstitution(double[][] ab) {
      int n = ab.length;
      double[] x = new double[n];
      x[n-1]  = ab[n-1][n]/ab[n-1][n-1];
      for (int i = n - 1; i >= 0; i--)
      {
        double cont = 0;
        for (int j = i + 1; j < n; j++)
        {
          cont+=(ab[i][j]*x[j]);
        }
        x[i] = (ab[i][n] - cont)/ab[i][i];
      }
      return x;
    }