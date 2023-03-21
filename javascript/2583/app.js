const fs = require('fs');

BOJkey = true;
let answer = 0;
let sizeArr = [];
let size = 0;
let input = fs
  .readFileSync(BOJkey ? './javascript/2583/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.split(' '))
  .map(el => el.map(Number));

const dfs = (i, j) => {
  if (i <= -1 || i >= N || j <= -1 || j >= M || graph[i][j] === 1) return;
  graph[i][j] = 1;
  size += 1;

  for (let k = 0; k < 4; k++) {
    const [ni, nj] = [i + dx[k], j + dy[k]];
    dfs(ni, nj);
  }
};

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

const [N, M, K] = input.shift();
const graph = Array.from({ length: N }, () => Array(M).fill(0));

for (let element of input) {
  const [leftBottomCol, leftBottomRow, rigthTopCol, rightTopRow] = element;
  for (let i = N - rightTopRow; i <= N - 1 - leftBottomRow; i++) {
    for (let j = leftBottomCol; j <= rigthTopCol - 1; j++) {
      graph[i][j] = 1;
    }
  }
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (graph[i][j] === 0) {
      size = 0;
      answer++;
      dfs(i, j);
      sizeArr.push(size);
    }
  }
}

console.log(answer);
console.log(sizeArr.sort((a, b) => a - b).join(' '));
