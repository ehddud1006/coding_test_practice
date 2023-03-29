const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/1946/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .reverse();

const answer = [];
const T = Number(input.pop());

for (let i = 0; i < T; i++) {
  const N = Number(input.pop());

  const data = [];
  for (let j = 0; j < N; j++) data.push(input.pop().split(' ').map(Number));
  data.sort((a, b) => a[0] - b[0]);

  let [target, count] = [Number.MAX_SAFE_INTEGER, 0];
  for (let j = 0; j < N; j++) {
    if (target > data[j][1]) {
      target = data[j][1];
      count++;
    }
  }

  answer.push(count);
}

console.log(answer.join('\n'));
