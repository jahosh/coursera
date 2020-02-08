import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private static final double DEFAULT_MULTIPLIER = 1.96;

    private final double[] results;

    private final int trials;

    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("N and T should be greater than zero!");
        }
        this.trials = trials;
        results = new double[trials];
        int square = n * n;
        for (int i = 0; i < trials; i++) {
            Percolation percolation = new Percolation(n);
            double numberOfOpenedCells = 0;
            while (!percolation.percolates()) {
                int x = StdRandom.uniform(n) + 1;
                int y = StdRandom.uniform(n) + 1;
                if (!percolation.isOpen(y, x)) {
                    percolation.open(y, x);
                    numberOfOpenedCells++;
                }
            }
            results[i] = numberOfOpenedCells / square;
        }
    }

    public double mean() {
        return StdStats.mean(results);
    }

    public double stddev() {
        return StdStats.stddev(results);
    }

    public double confidenceLo() {
        return mean() - (DEFAULT_MULTIPLIER * stddev() / Math.sqrt((double) trials));
    }

    public double confidenceHi() {
        return mean() + (DEFAULT_MULTIPLIER * stddev() / Math.sqrt((double) trials));
    }

    public static void main(String[] args) {
        PercolationStats ps = new PercolationStats(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
        System.out.print(String.format("Mean: %s\nStddev: %s\n96 confidence levels: [%s, %s]",
                ps.mean(), ps.stddev(), ps.confidenceLo(), ps.confidenceHi()));
    }
}
