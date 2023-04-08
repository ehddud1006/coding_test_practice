const fs = require('fs');

BOJkey = true;

const input = fs
  .readFileSync(BOJkey ? './javascript/5052re/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .reverse();

const T = Number(input.pop());
const answer = [];

for (let i = 0; i < T; i++) {
  const N = Number(input.pop());

  const testCase = [];
  const hash = {};
  for (let j = 0; j < N; j++) testCase.push(input.pop());
  testCase.sort();
  let flag = false;

  for (let k = 0; k < testCase.length; k++) {
    if (flag) {
      break;
    }

    let str = '';

    for (let x of testCase[k]) {
      str += x;
      if (hash[str]) {
        flag = true;
        break;
      }
    }

    hash[testCase[k]] = true;
  }

  if (flag) answer.push('NO');
  else answer.push('YES');
}

console.log(answer.join('\n'));
