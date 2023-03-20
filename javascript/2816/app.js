const fs = require('fs');

BOJkey = true;

let answer = '';
let input = fs
  .readFileSync(BOJkey ? './javascript/2816/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const N = input.shift();
answer += '1'.repeat(input.indexOf('KBS1')) + '4'.repeat(input.indexOf('KBS1'));
input = ['KBS1', ...input.slice(0, input.indexOf('KBS1')), ...input.slice(input.indexOf('KBS1') + 1)];
answer += '1'.repeat(input.indexOf('KBS2')) + '4'.repeat(input.indexOf('KBS2') - 1);

console.log(answer);
