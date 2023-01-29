const N = 9;
const arr = [32, 55, 62, 20, 250, 370, 200, 30, 100];

const reverseArr = arr.map(number => {
  let [digit, result] = [0, 0];
  while (number !== 0) {
    digit = number % 10;
    result = 10 * result + digit;
    number = parseInt(number / 10);
  }
  return result;
});

const isPrime = number => {
  if (number === 1) return false;
  for (let i = 2; i < Math.sqrt(number); i++) {
    if (number % i === 0) return false;
  }
  return true;
};

const answer = reverseArr.reduce((answer, number) => {
  if (isPrime(number)) answer.push(number);
  return answer;
}, []);

console.log(answer);
