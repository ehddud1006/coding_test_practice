const fs = require('fs');

BOJkey = 1;

const readInput = fs
  .readFileSync(BOJkey ? './코딩테스트강의/그래프와탐색/경로탐색인접리스트/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, M] = readInput.shift().split(' ').map(Number);
const graph = Array.from(Array(N + 1), () => Array());

const visited = Array.from(Array({ length: N + 1 }), () => false);
let count = 0;

const input = readInput.map(el => el.split(' ').map(Number));

for (const [a, b] of input) {
  graph[a].push(b);
}

function DFS(v) {
  if (v === N) {
    count++;
    return;
  }
  for (let i = 0; i < graph[v].length; i++) {
    let nextV = graph[v][i];
    if (!visited[nextV]) {
      visited[nextV] = true;
      DFS(nextV);
      visited[nextV] = false;
    }
  }
}

visited[1] = true;
DFS(1);

console.log(count);
