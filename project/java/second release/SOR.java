public class SOR {

    private double[] val;
    private int[] columns;
    private int[] firstRow;
    private double[] b;
    private double[] x;
    private double[] previousX;
    private double omega = 1.0;
    private final int maxits = 50;
    private int matrixSize;
    private double e;
    private int counter;
    private double tol = 1;
    private double residVal = 1;

    public SOR(int t, int matrixSize) {
        this.matrixSize = matrixSize;
        val = new double[t];
        columns = new int[t];
        firstRow = new int[matrixSize + 1];
        b = new double[matrixSize];
    }

    public void calculateInitialGuess() {
        x = divide();
        previousX = divide();

    }

    public void testDiagonal() {

        double diagVal = 0;
        double acumrow;
        int count = 0;
        for (int i = 0; i <= (matrixSize - 1); i++) // Each row
        {
            acumrow = 0;
            for (int j = firstRow[i]; j <= (firstRow[i + 1] - 1); j++) {
                if (columns[j] == i) {
                    diagVal = Math.abs(val[j]);
                } else {
                    acumrow += (Math.abs(val[j]));
                }
            }
            if (diagVal > acumrow) {
                count++;
            }
        }
    }

    private double calculateMachineEpsilon() {
        double machEps = 1.0;

        do {
            machEps /= 2.0;
        } while ((double) (1.0 + (machEps / 2.0)) != 1.0);

        return machEps;
    }

    public void performSOR() {
        double acum;
        double diagonal = 0;
        counter = 0;
        calculateInitialGuess();
        e = calculateMachineEpsilon();
        while (((residVal >= e) && (tol >= e)) && (counter <= maxits)) {
            for (int i = 0; i <= (matrixSize - 1); i++) {
                acum = 0;
                for (int j = firstRow[i]; j <= (firstRow[i + 1] - 1); j++) {
                    acum = acum + val[j] * x[columns[j]];

                    if (columns[j] == i) {
                        diagonal = val[j];
                    }
                }
                x[i] = x[i] + omega * (b[i] - acum) / diagonal;
                System.out.println("Iteration " + (counter + 1) + ", element "
                        + i + " : \t\t" + x[i]);
            }
            counter++;
            if (counter >= maxits) {
                checkConvergence_Divergence();
            }
        }

    }

    private void checkConvergence_Divergence() {

        residVal = calculateResidual(x);
        tol = successiveApprox(x);
    }

    private double successiveApprox(double[] x) {
        double successiveNorm;
        double subtraction[] = new double[matrixSize];
        double error[] = new double[matrixSize];

        for (int i = 0; i < matrixSize; i++) {
            subtraction[i] = ((x[i] - previousX[i]));
            error[i] = Math.abs((x[i] - previousX[i]) / x[i]) * 100;
            previousX[i] = x[i];
        }
        successiveNorm = calculateNorm(subtraction);
        return successiveNorm;
    }

    private double calculateResidual(double[] x) {
        double residual[] = new double[matrixSize];
        double[] mult = new double[matrixSize];
        double normResidual;

        mult = times(x);

        for (int i = 0; i < matrixSize; i++) {
            residual[i] = b[i] - mult[i];
        }
        normResidual = calculateNorm(residual);
        double bNorm = calculateNorm(b);
        return normResidual / bNorm;
    }

    private double calculateNorm(double[] x) {
        double acum = 0;
        for (int i = 0; i < matrixSize; i++) {
            acum = acum + x[i] * x[i];
        }
        return Math.sqrt(acum);

    }

    private double[] times(double[] x) {

        double[] times = new double[matrixSize];

        for (int i = 0; i < matrixSize; i++) {
            for (int j = firstRow[i]; j < firstRow[i + 1]; j++) {
                times[i] += val[j] * x[columns[j]];
            }
        }
        return times;
    }

    private double[] divide() {
        double[] divided = new double[matrixSize];
        for (int i = 0; i < matrixSize; i++) {
            for (int j = firstRow[i]; j < firstRow[i + 1]; j++) {
                divided[i] = b[i] / val[j];
            }
        }
        return divided;
    }

    public static double calculateMax(double[] error) {
        double maximum = error[0];
        for (int i = 1; i < error.length; i++) {
            if (error[i] > maximum) {
                maximum = error[i];
            }
        }
        return maximum;
    }

    public void populateCRS(double element, int index, int j) {
        val[index] = element;
        columns[index] = j;
    }

    public void populateRowStart(int i, int index) {
        firstRow[i + 1] = index;
    }

    public void populateVectorB(double element, int row) {
        b[row] = element;
    }
}
