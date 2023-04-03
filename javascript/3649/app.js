const fs = require('fs');

BOJkey = true;

const input = fs
  .readFileSync(BOJkey ? './javascript/3649/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number)
  .reverse();

const NANO_METER = 10_000_000;
const answer = [];

while (input.length > 0) {
  const widthHole = input.pop() * NANO_METER;
  const numberOfLegoPeices = input.pop();
  const legoPeices = [];

  for (let i = 0; i < numberOfLegoPeices; i++) {
    const legoPeice = input.pop();
    legoPeices.push(legoPeice);
  }

  legoPeices.sort((a, b) => a - b);

  let [lt, rt] = [0, numberOfLegoPeices];
  let flag = true;

  while (lt < rt) {
    if (widthHole === legoPeices[lt] + legoPeices[rt]) {
      answer.push(`yes ${legoPeices[lt]} ${legoPeices[rt]}`);
      flag = false;
      break;
    } else if (widthHole > legoPeices[lt] + legoPeices[rt]) {
      lt += 1;
    } else {
      rt -= 1;
    }
  }

  if (flag) answer.push(`danger`);
}

console.log(answer.join('\n'));
