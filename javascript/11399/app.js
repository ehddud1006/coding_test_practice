const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/11399/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.split(' ').map(Number));

const [N] = input.shift();

const arr = input.pop();

arr.sort((a, b) => a - b);

let acc = 0;
let answer = 0;
for (let i = 0; i < N; i++) {
  acc += arr[i];
  answer += acc;
}

console.log(answer);
