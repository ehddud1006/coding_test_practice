const fs = require('fs');

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? './코딩테스트강의/DFS/바둑이승차/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [C, N] = input.shift().split(' ').map(Number);
input = input.map(Number);
let max = Number.MIN_SAFE_INTEGER;

function dfs(L, sum) {
  if (sum > C) return;
  if (L === N) {
    max = Math.max(sum, max);
    return;
  }

  dfs(L + 1, sum + input[L]);
  dfs(L + 1, sum);
}

dfs(0, 0);

console.log(max);
