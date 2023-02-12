const fs = require('fs');

BOJkey = 1;

const readInput = fs
  .readFileSync(BOJkey ? './코딩테스트강의/그래프와탐색/경로탐색/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, M] = readInput.shift().split(' ').map(Number);
const graph = Array.from(Array(N + 1), () => Array(N + 1).fill(0));
const visited = Array.from(Array({ length: N + 1 }), () => false);
let count = 0;

const input = readInput.map(el => el.split(' ').map(Number));

for (let [a, b] of input) {
  graph[a][b] = 1;
}

function dfs(v) {
  if (v === 5) {
    count++;
    return;
  }

  for (let i = 1; i <= 5; i++) {
    if (!visited[i] && graph[v][i] === 1) {
      visited[i] = true;
      dfs(i);
      visited[i] = false;
    }
  }
}

visited[1] = true;
dfs(1);

console.log(count);
