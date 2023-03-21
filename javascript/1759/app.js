const fs = require('fs');

BOJkey = true;
let input = fs
  .readFileSync(BOJkey ? './javascript/1759/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const JA = 'bcdfghjklmnpqrstvwxyz';
const MO = 'aeiou';
const [M, C] = input.shift().split(' ').map(Number);
input = input.pop().split(' ');

console.log(input);

const visited = Array.from({ length: C }, () => false);
const temp = [];
answer = [];
const dfs = (L, S) => {
  if (L === M) {
    answer.push([...temp].sort().join(''));
    return;
  }
  for (let i = S; i < C; i++) {
    temp.push(input[i]);
    dfs(L + 1, i + 1);
    temp.pop();
  }
};

dfs(0, 0);

let realAnswer = '';
for (let str of answer.sort()) {
  let jaCount = 0;
  let moCount = 0;

  for (let x of JA) {
    if (str.includes(x)) jaCount++;
  }

  for (let x of MO) {
    if (str.includes(x)) moCount++;
  }

  if (jaCount >= 2 && moCount >= 1) realAnswer += str + '\n';
}

console.log(realAnswer);
