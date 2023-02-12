const N = 9;
const arr = [32, 55, 62, 20, 250, 370, 200, 30, 100];
const answer = [];

function isPrime(number) {
  if (number === 1) return false;

  for (let i = 2; i < Math.sqrt(number); i++) {
    if (number % i === 0) return false;
  }
  return true;
}

arr.forEach(number => {
  let res = 0;
  while (number !== 0) {
    let na = number % 10;
    number = parseInt(number / 10);
    res = res * 10 + na;
  }
  if (isPrime(res)) answer.push(res);
});

console.log(answer);
