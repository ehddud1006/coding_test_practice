const Compare = {
  LESS_THAN: -1,
  BIGGER_THAN: 1,
  EQUALS: 0,
};

const DOES_NOT_EXIST = -1;

function lesserEquals(a, b, compareFn) {
  const comp = compareFn(a, b);
  return comp === Compare.LESS_THAN || comp === Compare.EQUALS;
}

function biggerEquals(a, b, compareFn) {
  const comp = compareFn(a, b);
  return comp === Compare.BIGGER_THAN || comp === Compare.EQUALS;
}

function defaultCompare(a, b) {
  if (a === b) {
    return Compare.EQUALS;
  }
  return a < b ? Compare.LESS_THAN : Compare.BIGGER_THAN;
}

function defaultEquals(a, b) {
  return a === b;
}

function defaultToString(item) {
  if (item === null) {
    return "NULL";
  }
  if (item === undefined) {
    return "UNDEFINED";
  }
  if (typeof item === "string" || item instanceof String) {
    return `${item}`;
  }
  return item.toString();
}

function swap(array, a, b) {
  /* const temp = array[a];
    array[a] = array[b];
    array[b] = temp; */
  [array[a], array[b]] = [array[b], array[a]];
}
function reverseCompare(compareFn) {
  return (a, b) => compareFn(b, a);
}

function defaultDiff(a, b) {
  return Number(a) - Number(b);
}

class MinHeap {
  constructor(compareFn = defaultCompare) {
    this.compareFn = compareFn;
    this.heap = [];
  }

  getLeftIndex(index) {
    return 2 * index + 1;
  }

  getRightIndex(index) {
    return 2 * index + 2;
  }

  getParentIndex(index) {
    if (index === 0) {
      return undefined;
    }
    return Math.floor((index - 1) / 2);
  }

  size() {
    return this.heap.length;
  }

  isEmpty() {
    return this.size() <= 0;
  }

  clear() {
    this.heap = [];
  }

  findMinimum() {
    return this.isEmpty() ? undefined : this.heap[0];
  }

  insert(value) {
    if (value != null) {
      const index = this.heap.length;
      this.heap.push(value);
      this.siftUp(index);
      return true;
    }
    return false;
  }

  siftDown(index) {
    let element = index;
    const left = this.getLeftIndex(index);
    const right = this.getRightIndex(index);
    const size = this.size();
    if (
      left < size &&
      this.compareFn(this.heap[element], this.heap[left]) ===
        Compare.BIGGER_THAN
    ) {
      element = left;
    }
    if (
      right < size &&
      this.compareFn(this.heap[element], this.heap[right]) ===
        Compare.BIGGER_THAN
    ) {
      element = right;
    }
    if (index !== element) {
      swap(this.heap, index, element);
      this.siftDown(element);
    }
  }

  siftUp(index) {
    let parent = this.getParentIndex(index);
    while (
      index > 0 &&
      this.compareFn(this.heap[parent], this.heap[index]) ===
        Compare.BIGGER_THAN
    ) {
      swap(this.heap, parent, index);
      index = parent;
      parent = this.getParentIndex(index);
    }
  }

  extract() {
    if (this.isEmpty()) {
      return undefined;
    }
    if (this.size() === 1) {
      return this.heap.shift();
    }
    const removedValue = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.siftDown(0);
    return removedValue;
  }

  heapify(array) {
    if (array) {
      this.heap = array;
    }
    const maxIndex = Math.floor(this.size() / 2) - 1;
    for (let i = 0; i <= maxIndex; i++) {
      this.siftDown(i);
    }
    return this.heap;
  }

  getAsArray() {
    return this.heap;
  }
}
class MaxHeap extends MinHeap {
  constructor(compareFn = defaultCompare) {
    super(compareFn);
    this.compareFn = compareFn;
    this.compareFn = reverseCompare(compareFn);
  }
}

const fs = require("fs");

BOJkey = false;

let input = fs
  .readFileSync(BOJkey ? "./javascript/11279js/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let number = input.shift();
const maxHeap = new MaxHeap();
let result = [];
for (let i = 0; i < number; i++) {
  if (input[i] === "0") {
    if (maxHeap.isEmpty()) {
      result.push(0);
    } else {
      result.push(maxHeap.extract());
    }
  } else {
    maxHeap.insert(+input[i]);
  }
}

console.log(result.join("\n"));
