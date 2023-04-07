const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/1987re/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, M] = input.shift().split(' ').map(Number);

const visited = Array.from({ length: 26 }, () => false);
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

input = input.map(item => item.split(''));
let maxx = Number.MIN_SAFE_INTEGER;

const dfs = (x, y, L) => {
  if (x < 0 || y < 0 || x >= N || y >= M || visited[input[x][y].charCodeAt() - 65]) return;

  visited[input[x][y].charCodeAt() - 65] = true;
  maxx = Math.max(maxx, L);

  dfs(x - 1, y, L + 1);
  dfs(x, y + 1, L + 1);
  dfs(x + 1, y, L + 1);
  dfs(x, y - 1, L + 1);

  visited[input[x][y].charCodeAt() - 65] = false;
};

dfs(0, 0, 1);
console.log(maxx);
