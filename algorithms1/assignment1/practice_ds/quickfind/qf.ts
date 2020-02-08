class QuickFind {

  storage: number[];

  size: number;

  constructor(size) {
    this.storage = this._initStorageArray(size)
    this.size = size;
  }

  private _initStorageArray(size: number) {
    const storage = []
    for (let i = 0; i < size; i++) {
      storage[i] = i
    }
    return storage;
  }

  private _checkIndicies(a: number, b: number) {
    if (a > this.size || b > this.size) {
      throw new Error("Index out of range error. Please check index a or b and try again.")
    }
  }

  isConnected(a: number, b: number) {
    this._checkIndicies(a, b);
    return this.storage[a] == this.storage[b];
  }

  union(a: number, b: number) {
    this._checkIndicies(a, b);
    const aRoot = this.storage[a];
    const bRoot = this.storage[b];
    for (let i = 0; i < this.storage.length; i++) {
      if (this.storage[i] === bRoot) {
        this.storage[i] = aRoot;
      }
    }
  }
}