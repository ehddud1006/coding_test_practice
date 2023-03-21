const fs = require('fs');

BOJkey = true;
let input = fs
  .readFileSync(BOJkey ? './javascript/2309/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

const temp = [];
let answer = [];
let flag = false;
const dfs = (L, S) => {
  if (flag) return;
  if (L === 7) {
    const sum = temp.reduce((acc, cur) => {
      return acc + cur;
    }, 0);

    if (sum === 100) {
      flag = true;
      answer = [...temp];
    }
    return;
  }
  for (let i = S; i < 9; i++) {
    temp.push(input[i]);
    dfs(L + 1, i + 1);
    temp.pop();
  }
};

dfs(0, 0);

answer.sort((a, b) => a - b);
console.log(answer.join('\n'));
