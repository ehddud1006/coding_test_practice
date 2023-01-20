const fs = require('fs');

BOJkey = 1;

const input = fs
  .readFileSync(BOJkey ? './코딩테스트강의/DFS/중복순열구하기/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.split(' ').map(Number));

const [N, M] = input.shift();
const temp = [];
let count = 0;
let answer = '';
function dfs(L) {
  if (L == M) {
    count++;
    answer += temp.join(' ') + '\n';
    return;
  }
  for (let i = 1; i <= N; i++) {
    temp.push(i);
    dfs(L + 1);
    temp.pop();
  }
}

dfs(0);
answer += count.toString();
console.log(answer);
