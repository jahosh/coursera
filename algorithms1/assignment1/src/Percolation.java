import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private final WeightedQuickUnionUF weightedQuickUnion;
    private final WeightedQuickUnionUF weightedQuickUnionBackwash;
    private final boolean[] opened;
    private final int size;
    private int numberOfOpenSites;

    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("N must be greater than 0");
        }

        size = n;


        weightedQuickUnion = new WeightedQuickUnionUF((n * n) + 2);
        weightedQuickUnionBackwash = new WeightedQuickUnionUF((n * n) + 2);
        opened = new boolean[(n * n) + 2];
        numberOfOpenSites = 0;

        for (int i = 1; i < n + 1; i++) {
            weightedQuickUnion.union(0, i);
            weightedQuickUnion.union(n * n + 1, n * n + 1 - i);
            weightedQuickUnionBackwash.union(0, i);
        }

    }

    public boolean isOpen(int row, int col) {
        this.checkIndicies(row, col);
        return opened[xyTo1D(row, col)];
    }

    public void open(int row, int col) {
        this.checkIndicies(row, col);

        if (isOpen(row, col)) {
            return;
        }

        int arrayIndex = xyTo1D(row, col);
        opened[arrayIndex] = true;
        this.numberOfOpenSites++;

        // check if should union left
        if (row > 1 && this.isOpen(row - 1, col)) {
            weightedQuickUnion.union(xyTo1D(row, col), xyTo1D(row - 1, col));
            weightedQuickUnionBackwash.union(xyTo1D(row, col), xyTo1D(row - 1, col));
        }

        // check if should union right
        if (row < size && this.isOpen(row + 1, col)) {
            weightedQuickUnion.union(xyTo1D(row, col), xyTo1D(row + 1, col));
            weightedQuickUnionBackwash.union(xyTo1D(row, col), xyTo1D(row + 1, col));
        }

        // check if should union top
        if (col < size && this.isOpen(row, col + 1)) {
            weightedQuickUnion.union(xyTo1D(row, col), xyTo1D(row, col + 1));
            weightedQuickUnionBackwash.union(xyTo1D(row, col), xyTo1D(row, col + 1));
        }

        // check if should union bottom
        if (col > 1 && this.isOpen(row, col - 1)) {
            weightedQuickUnion.union(xyTo1D(row, col), xyTo1D(row, col - 1));
            weightedQuickUnionBackwash.union(xyTo1D(row, col), xyTo1D(row, col - 1));
        }
    }

    public int numberOfOpenSites() {
        return numberOfOpenSites;
    }

    public boolean percolates() {
        return this.numberOfOpenSites > 0 && weightedQuickUnion.find(0) == weightedQuickUnion.find(size * size + 1);
    }

    private void checkIndicies(int row, int col) {
        if (row <= 0 || row > size || col <= 0 || col > size) {
            throw new IllegalArgumentException("row or col is outside index range.");
        }
    }

    public boolean isFull(int row, int col) {
        this.checkIndicies(row, col);
        return weightedQuickUnionBackwash.find(0) == weightedQuickUnionBackwash.find(xyTo1D(row, col)) && isOpen(row, col);

    }

    /**
     * Converts 2d indices into 1d index
     */
    private int xyTo1D(int row, int col) {
        return (size * (row - 1) + (col - 1) + 1);
    }
}
