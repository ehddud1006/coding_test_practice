const fs = require('fs');

BOJkey = 1;

const [N, K] = fs
  .readFileSync(BOJkey ? './코딩테스트강의/DFS/바둑이승차/input.txt' : './dev/stdin')
  .toString()
  .split(' ')
  .map(Number);

const temp = [];
let answer = '';
const dfs = L => {
  if (L === K) {
    answer += temp.join(' ') + '\n';
    return;
  }

  for (let i = 1; i <= N; i++) {
    temp.push(i);
    dfs(L + 1);
    temp.pop();
  }
};

dfs(0);

console.log(answer.slice(0, answer.length - 1));
