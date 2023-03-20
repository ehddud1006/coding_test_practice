const fs = require('fs');

BOJkey = true;

let [row, col] = [0, 0];
let input = fs
  .readFileSync(BOJkey ? './javascript/1652/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const N = Number(input.shift());

input = input.map(element => element.split(''));

// 가로 체크
for (let i = 0; i < N; i++) {
  let count = 0;

  for (let j = 0; j < N; j++) {
    if (input[i][j] === '.') count++;
    if (input[i][j] === 'X') {
      if (count >= 2) row++;
      count = 0;
    }
  }

  if (count >= 2) row++;
}

for (let i = 0; i < N; i++) {
  let count = 0;

  for (let j = 0; j < N; j++) {
    if (input[j][i] === '.') count++;
    if (input[j][i] === 'X') {
      if (count >= 2) col++;
      count = 0;
    }
  }

  if (count >= 2) col++;
}

console.log(`${row} ${col}`);
