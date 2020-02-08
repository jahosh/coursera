class QuickUnion {

  storage: number[];

  size: number;

  constructor(size: number) {
    this.storage = this.initStorageArray(size);
    this.size = size;
  }

  private initStorageArray(size: number) {
    const storage = [];
    for (let i = 0; i < size; i++) {
      storage[i] = i
    }
    return storage;
  }

  private checkIndicies(a: number, b: number) {
    if (a > this.size || b > this.size) {
      throw new Error("Index ouit of range error. Please check index of a or b and try again.");
    }
  }

  private getRoots(a: number, b: number) {
    let aRoot = a;
    let bRoot = b;
    while (this.storage[aRoot] !== aRoot || this.storage[bRoot] !== bRoot) {
      aRoot = this.storage[aRoot];
      bRoot = this.storage[bRoot];
    }
    return [aRoot, bRoot];
  }

  isConnected(a: number, b: number) {
    this.checkIndicies(a, b);
    const [ aRoot, bRoot ] = this.getRoots(a, b);
    return aRoot === bRoot;
  }

  union(a: number, b: number) {
    this.checkIndicies(a, b);
    const [ aRoot, bRoot ] = this.getRoots(a, b);
    this.storage[bRoot] = aRoot;
  }


}