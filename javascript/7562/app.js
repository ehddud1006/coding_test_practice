class Queue {
  constructor() {
    this.count = 0;
    this.lowestCount = 0;
    this.items = {};
  }

  enqueue(element) {
    this.items[this.count] = element;
    this.count++;
  }

  dequeue() {
    if (this.isEmpty()) {
      return undefined;
    }
    const result = this.items[this.lowestCount];
    delete this.items[this.lowestCount];
    this.lowestCount++;
    return result;
  }

  peek() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.lowestCount];
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
      return '';
    }
    let objString = `${this.items[this.lowestCount]}`;
    for (let i = this.lowestCount + 1; i < this.count; i++) {
      objString = `${objString},${this.items[i]}`;
    }
    return objString;
  }
}

const dx = [-2, -1, 1, 2, 2, 1, -1, -2];
const dy = [1, 2, 2, 1, -1, -2, -2, -1];

const fs = require('fs');

BOJkey = true;
let input = fs
  .readFileSync(BOJkey ? './javascript/7562/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const answer = [];
const T = input.shift();

for (let i = 0; i < T; i++) {
  const size = Number(input.shift());
  const [nowX, nowY] = input.shift().split(' ').map(Number);
  const [goalX, goalY] = input.shift().split(' ').map(Number);

  let visited = Array.from({ length: size }, () => Array(size).fill(false));
  const queue = new Queue();
  queue.enqueue([nowX, nowY, 0]);

  while (!queue.isEmpty()) {
    const [x, y, step] = queue.dequeue();

    if (x === goalX && y === goalY) {
      answer.push(step);
      break;
    }

    for (let j = 0; j < 8; j++) {
      const [nx, ny] = [x + dx[j], y + dy[j]];

      if (nx >= 0 && nx < size && ny >= 0 && ny < size && !visited[nx][ny]) {
        visited[nx][ny] = true;
        queue.enqueue([nx, ny, step + 1]);
      }
    }
  }
}

console.log(answer.join('\n'));
