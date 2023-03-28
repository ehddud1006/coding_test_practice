const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/5052/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .reverse();

const answer = [];

const T = Number(input.pop());

for (let i = 0; i < T; i++) {
  const N = Number(input.pop());
  const phoneMap = {};
  let consistency = 'YES';
  const arr = [];

  for (let j = 0; j < N; j++) arr.push(input.pop());

  arr.sort();

  for (let j = 0; j < N; j++) {
    const phone = arr[j];
    let str = [];
    let flag = false;

    for (let digit of phone) {
      str.push(digit);
      if (phoneMap[str.join('')] !== undefined) {
        consistency = 'NO';
        flag = true;
        break;
      }
    }

    if (flag) break;

    phoneMap[phone] = 1;
  }
  answer.push(consistency);
}

console.log(answer.join('\n'));
