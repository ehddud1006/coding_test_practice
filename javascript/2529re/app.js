const fs = require('fs');

BOJkey = true;

const input = fs
  .readFileSync(BOJkey ? './javascript/2529re/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const N = Number(input.shift());
const inequalitySign = input.pop().split(' ');

const temp = [];
const visited = Array.from({ length: 10 }, () => false);
const answer = [];

const dfs = L => {
  if (L === N + 1) {
    for (let i = 0; i < inequalitySign.length; i++) {
      if (inequalitySign[i] === '<' && temp[i] > temp[i + 1]) return;
      if (inequalitySign[i] === '>' && temp[i] < temp[i + 1]) return;
    }
    answer.push(Number(temp.join('')));
    return;
  }

  for (let i = 0; i < 10; i++) {
    if (!visited[i]) {
      visited[i] = true;
      temp.push(i);
      dfs(L + 1);
      temp.pop();
      visited[i] = false;
    }
  }
};

dfs(0);

answer.sort((a, b) => a - b);
console.log(
  answer
    .at(-1)
    .toString()
    .padStart(N + 1, '0'),
);
console.log(answer[0].toString().padStart(N + 1, '0'));
