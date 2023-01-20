const fs = require('fs');

BOJkey = 1;

const input = fs
  .readFileSync(BOJkey ? './코딩테스트강의/DFS/동전교환/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const N = Number(input[0]);
const kind = input[1].split(' ').map(Number);
const M = Number(input[2]);

let answer = Number.MAX_SAFE_INTEGER;

function dfs(M, count) {
  if (M < 0) return;
  if (M === 0) {
    answer = Math.min(answer, count);
  }
  for (let i = 0; i < N; i++) {
    dfs(M - kind[i], count + 1);
  }
}

dfs(M, 0);

console.log(answer);
