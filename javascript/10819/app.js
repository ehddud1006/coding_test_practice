const fs = require('fs');

BOJkey = true;
let input = fs
  .readFileSync(BOJkey ? './javascript/10819/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const N = Number(input.shift());

input = input.pop().split(' ').map(Number);
const visited = Array.from({ length: N + 1 }, () => false);
const temp = [];
let answer = Number.MIN_SAFE_INTEGER;
const dfs = L => {
  if (L === N) {
    let sum = 0;
    for (let j = 0; j < N - 1; j++) {
      sum += Math.abs(temp[j] - temp[j + 1]);
    }

    answer = Math.max(sum, answer);
  }
  for (let i = 0; i < N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      temp.push(input[i]);
      dfs(L + 1);
      visited[i] = false;
      temp.pop();
    }
  }
};

dfs(0);

console.log(answer);
