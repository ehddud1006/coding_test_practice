const fs = require('fs');

BOJkey = true;
let answer = 0;
let input = fs
  .readFileSync(BOJkey ? './javascript/11724/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.split(' ').map(Number));

const [N, M] = input.shift();
const visited = Array.from({ length: N + 1 }, () => false);
const graph = Array.from({ length: N + 1 }, () => Array());

for (let [a, b] of input) {
  graph[a].push(b);
  graph[b].push(a);
}

const dfs = v => {
  for (let i = 0; i < graph[v].length; i++) {
    if (!visited[graph[v][i]]) {
      visited[graph[v][i]] = true;
      dfs(graph[v][i]);
    }
  }
};

for (let i = 1; i <= N; i++) {
  if (!visited[i]) {
    answer++;
    visited[i] = true;
    dfs(i);
  }
}

console.log(answer);
