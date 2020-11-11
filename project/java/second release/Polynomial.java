public class Polynomial {

    private double[] coefficients;

    public Polynomial() {
        coefficients = new double[1];
        coefficients[0] = 1;
    }

    public Polynomial(double[] c) {
        coefficients = c;
    }

    public Polynomial divide(double c) {
        double res[] = new double[getGrade()];
        for (int i = 0; i < getGrade(); i++)
                res[i] = coefficients[i] / c;
        return new Polynomial(res);            
    }

    public Polynomial times(Polynomial p) {
        int n = getGrade(), m = p.getGrade();
        double[] res = new double[n + m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                res[i+j] += getCoefficients()[i] * p.getCoefficients()[j];
            }
        }
        return new Polynomial(res);
    }

    public double evaluate(double x) {
        double acum = 0;
        for (int i = 0; i < getGrade(); i++) {
            acum += coefficients[i] * Math.pow(x, i);
        }
        return acum;
    }

    public double[] getCoefficients() {
        return coefficients;
    }

    public int getGrade() {
        return coefficients.length;
    }

}
