const fs = require('fs');

BOJkey = 1;

const input = fs
  .readFileSync(BOJkey ? './코딩테스트강의/DFS/순열구하기/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
const visit = Array.from({ length: N }, () => false);
const answer = Array.from({ length: M }, () => 0);
let count = 0;
function dfs(L) {
  if (L === M) {
    count++;
    console.log(answer.join(' '));
    return;
  }
  for (let i = 0; i < N; i++) {
    if (!visit[i]) {
      answer[L] = arr[i];
      visit[i] = true;
      dfs(L + 1);
      visit[i] = false;
    }
  }
}

dfs(0);
console.log(count);
