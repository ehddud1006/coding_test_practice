const fs = require('fs');

BOJkey = 1;

const input = fs
  .readFileSync(BOJkey ? './코딩테스트강의/DFS/최대점수구하기/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.split(' ').map(Number));

const [N, M] = input.shift();

let max = Number.MIN_SAFE_INTEGER;
function dfs(L, score, time) {
  if (time > M) return;
  if (L === N) {
    max = Math.max(max, score);
    return;
  }
  dfs(L + 1, score + input[L][0], time + input[L][1]);
  dfs(L + 1, score, time);
}

dfs(0, 0, 0);

console.log(max);
