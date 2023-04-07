const fs = require('fs');

BOJkey = true;

let answer = '';
let input = fs
  .readFileSync(BOJkey ? './javascript/2589re/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

class Node {
  constructor(x, y, dist = -1) {
    this.x = x;
    this.y = y;
    this.dist = dist;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }
  push(value) {
    const node = new Node(value.x, value.y, value?.dist);
    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.size++;
  }
  shift() {
    if (!this.size) return null;
    const node = this.head;
    if (this.head === this.tail) {
      this.tail = null;
    }
    this.head = this.head.next;
    this.size--;
    return node;
  }
}
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];
const q = new Queue();

const [N, M] = input.shift().split(' ').map(Number);
input = input.map(item => item.split(''));

let mmax = Number.MIN_SAFE_INTEGER;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (input[i][j] === 'L') {
      const q = new Queue();
      const visited = Array.from({ length: N }, () => Array(M).fill(false));

      visited[i][j] = true;
      q.push({ x: i, y: j, dist: 0 });

      while (q.size) {
        const { x, y, dist } = q.shift();
        mmax = Math.max(dist, mmax);

        for (let i = 0; i < 4; i++) {
          const nx = x + dx[i];
          const ny = y + dy[i];

          if (nx >= 0 && ny >= 0 && nx < N && ny < M && input[nx][ny] === 'L' && !visited[nx][ny]) {
            q.push({ x: nx, y: ny, dist: dist + 1 });
            visited[nx][ny] = true;
          }
        }
      }
    }
  }
}

console.log(mmax);
