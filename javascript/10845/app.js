class Deque {
  constructor() {
    this.count = 0;
    this.lowestCount = 0;
    this.items = {};
  }

  addFront(element) {
    if (this.isEmpty()) {
      this.addBack(element);
    } else if (this.lowestCount > 0) {
      this.lowestCount--;
      this.items[this.lowestCount] = element;
    } else {
      for (let i = this.count; i > 0; i--) {
        this.items[i] = this.items[i - 1];
      }
      this.count++;
      this.items[0] = element;
    }
  }

  addBack(element) {
    this.items[this.count] = element;
    this.count++;
  }

  removeFront() {
    if (this.isEmpty()) {
      return undefined;
    }
    const result = this.items[this.lowestCount];
    delete this.items[this.lowestCount];
    this.lowestCount++;
    return result;
  }

  removeBack() {
    if (this.isEmpty()) {
      return undefined;
    }
    this.count--;
    const result = this.items[this.count];
    delete this.items[this.count];
    return result;
  }

  peekFront() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.lowestCount];
  }

  peekBack() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.count - 1];
  }

  isEmpty() {
    return this.size() === 0;
  }

  clear() {
    this.items = {};
    this.count = 0;
    this.lowestCount = 0;
  }

  size() {
    return this.count - this.lowestCount;
  }

  toString() {
    if (this.isEmpty()) {
      return "";
    }
    let objString = `${this.items[this.lowestCount]}`;
    for (let i = this.lowestCount + 1; i < this.count; i++) {
      objString = `${objString},${this.items[i]}`;
    }
    return objString;
  }
}
const fs = require("fs");

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/10845/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let number = input.shift();
const queue = new Deque();
let result = [];

for (let i = 0; i < number; i++) {
  let command = input[i].split(" ");
  switch (command[0]) {
    case "push":
      queue.addBack(command[1]);
      break;
    case "front":
      let front = queue.peekFront();
      if (front) {
        result.push(front);
      } else {
        result.push("-1");
      }
      break;
    case "back":
      let back = queue.peekBack();
      if (back) {
        result.push(back);
      } else {
        result.push("-1");
      }
      break;
    case "size":
      result.push(queue.size());
      break;

    case "empty":
      if (!queue.size()) {
        result.push("1");
      } else {
        result.push("0");
      }
      break;
    case "pop":
      let pop = queue.removeFront();
      if (pop) {
        result.push(pop);
      } else {
        result.push("-1");
      }
      break;
  }
}

console.log(result.join("\n"));
