const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/1449/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.split(' ').map(Number));

const [N, L] = input.shift();
const target = input.pop();
let [tape, count] = [0, 0];
target.sort((a, b) => a - b);

target.forEach(position => {
  if (position > tape) {
    tape = position + L - 1;
    count++;
  }
});

console.log(count);
