const fs = require('fs');

BOJkey = true;

let answer = '';
let input = fs
  .readFileSync(BOJkey ? './javascript/2816re/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const N = input.shift();

const kbs1Index = input.indexOf('KBS1');
const kbs2Index = input.indexOf('KBS2');

if (kbs2Index > kbs1Index) {
  answer += '1'.repeat(kbs1Index);
  answer += '4'.repeat(kbs1Index - 0);
  answer += '1'.repeat(kbs2Index);
  answer += '4'.repeat(kbs2Index - 1);
} else {
  answer += '1'.repeat(kbs1Index);
  answer += '4'.repeat(kbs1Index - 0);
  answer += '1'.repeat(kbs2Index + 1);
  answer += '4'.repeat(kbs2Index);
}

console.log(answer);
