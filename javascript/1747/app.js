const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/1747/input.txt' : './dev/stdin')
  .toString()
  .trim();

let answer = '';
for (let i = Number(input); i <= Number.MAX_SAFE_INTEGER; i++) {
  let primeCheck = true;
  let pelindromCheck = false;
  for (let j = 2; j <= Math.sqrt(i); j++) {
    if (i % j === 0) {
      primeCheck = false;
      break;
    }
  }

  if (primeCheck) {
    let target = i.toString();
    let targetReverse = target.split('').reverse().join('');

    if (target === targetReverse) pelindromCheck = true;
  }

  if (i !== 1 && primeCheck && pelindromCheck) {
    answer = i;
    break;
  }
}

console.log(answer);
