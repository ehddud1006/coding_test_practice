const fs = require('fs');

BOJkey = true;

const input = fs
  .readFileSync(BOJkey ? './javascript/1747re/input.txt' : './dev/stdin')
  .toString()
  .trim();

let N = Number(input);

const isPelindrom = number => {
  if (number.toString() === number.toString().split('').reverse().join('')) return true;
  return false;
};

while (true) {
  if (N === 1) {
    N++;
    continue;
  }

  if (N > 1_000_000) {
    console.log(1003001);
    break;
  }

  let isPrime = true;

  if (isPelindrom(N)) {
    for (let i = 2; i <= Math.sqrt(N); i++) {
      if (N % i === 0) {
        isPrime = false;
        break;
      }
    }

    if (isPrime) {
      console.log(N);
      break;
    }
  }

  N++;
}
