   public static double[][] PartialPivoting(double[][] a, int k) { 
      double great=  Math.abs(a[k][k]);
      int fGreat= k;
      int n = a.length;
      for (int i = k + 1; i < n; i++)
      {
        if(Math.abs(a[i][k]) > great)
        {
          great= a[i][k];
          fGreat=  i;
        }
      }
      if (great== 0) System.out.println("The system doesn't have unic answer");
      else if (fGreat != k)
      {
        swapRows(a,fGreat ,k);
      }
      return a;
    }