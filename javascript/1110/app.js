const fs = require('fs');

BOJkey = true;
let answer = 0;
let input = Number(
  fs
    .readFileSync(BOJkey ? './javascript/1110/input.txt' : './dev/stdin')
    .toString()
    .trim(),
);
const N = input;

const dfs = (number, L) => {
  if (number === N && L > 0) {
    answer = L;
    return;
  }

  let rightNumber = number.toString().split('').at(-1);

  if (number < 10) {
    newNumber = number.toString();
  } else {
    const [first, second] = number.toString().split('');
    newNumber = (Number(first) + Number(second)).toString();
  }

  let newNumberRight = newNumber.toString().split('').at(-1);
  dfs(Number(rightNumber + newNumberRight), L + 1);
};

dfs(input, 0);

console.log(answer);
