const fs = require('fs');

BOJkey = 1;

let N = fs.readFileSync(BOJkey ? './코딩테스트강의/DFS/바둑이승차/input.txt' : './dev/stdin').toString();

N = Number(N);

const visited = Array.from({ length: N + 1 }, () => false);
const temp = [];
let answer = '';
const dfs = L => {
  if (L === N) {
    answer += temp.join(' ') + '\n';
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      temp.push(i);
      dfs(L + 1);
      visited[i] = false;
      temp.pop();
    }
  }
};

dfs(0);

console.log(answer.slice(0, answer.length - 1));
