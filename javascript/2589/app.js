class Node {
  constructor(item) {
    this.x = item.x;
    this.y = item.y;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.front = null;
    this.rear = null;
    this.size = 0;
  }

  enQueue(item) {
    const node = new Node(item);
    if (this.front === null) {
      this.front = node;
      this.front.next = this.rear;
    } else this.rear.next = node;
    this.rear = node;
    this.size += 1;
  }

  deQueue() {
    if (this.size === 1) {
      const temp = {
        x: this.front.x,
        y: this.front.y,
        depth: this.front.depth,
      };
      this.front = null;
      this.rear = null;
      this.size -= 1;
      return temp;
    } else if (this.size === 2) {
      const temp = {
        x: this.front.x,
        y: this.front.y,
        depth: this.front.depth,
      };
      const front = this.front.next;
      this.front = front;
      this.rear = front;
      this.size -= 1;
      return temp;
    } else if (this.size > 2) {
      const temp = {
        x: this.front.x,
        y: this.front.y,
        depth: this.front.depth,
      };
      this.front = this.front.next;
      this.size -= 1;
      return temp;
    }
  }

  getSize() {
    return this.size;
  }

  printFront() {
    return { x: this.front.x, y: this.front.y, depth: this.front.depth };
  }

  printBack() {
    return { x: this.rear.x, y: this.rear.y, depth: this.rear.depth };
  }
}

const fs = require('fs');

BOJkey = true;
let input = fs
  .readFileSync(BOJkey ? './javascript/2589/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];
let answer = Number.MIN_SAFE_INTEGER;
const [N, M] = input.shift().split(' ').map(Number);
input = input.map(el => el.split('')).map(line => line.map(el => (el === 'L' ? 0 : -1)));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (input[i][j] === 0) {
      const queue = new Queue();

      const graph = [];
      for (let l = 0; l < N; l++) {
        graph.push([...input[l]]);
      }

      queue.enQueue({ x: i, y: j });

      while (queue.getSize()) {
        const node = queue.deQueue();
        const [x, y] = [node.x, node.y];

        for (let k = 0; k < 4; k++) {
          const [nx, ny] = [x + dx[k], y + dy[k]];

          if (nx === i && ny === j) continue;

          if (nx > -1 && nx < N && ny > -1 && ny < M && graph[nx][ny] === 0) {
            graph[nx][ny] = graph[x][y] + 1;
            queue.enQueue({ x: nx, y: ny });
          }
        }
      }

      answer = Math.max(answer, ...graph.flat());
    }
  }
}

console.log(answer);
