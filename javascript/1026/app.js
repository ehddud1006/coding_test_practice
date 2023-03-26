const fs = require('fs');

BOJkey = false;

let input = fs
  .readFileSync(BOJkey ? './javascript/1026/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.split(' ').map(Number));

const [N] = input.shift();

ascArr = input.shift().sort((a, b) => a - b);
descArr = input.pop().sort((a, b) => b - a);

let answer = 0;
for (let i = 0; i < N; i++) {
  answer += ascArr[i] * descArr[i];
}

console.log(answer);
