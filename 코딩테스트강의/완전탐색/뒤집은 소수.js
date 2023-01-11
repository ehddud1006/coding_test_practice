const N = 9;
const arr = [32, 55, 62, 20, 250, 370, 200, 30, 100];

const isPrime = number => {
  if (number === 1) return false;

  for (let i = 2; i < parseInt(Math.sqrt(number)); i++) {
    if (number % i === 0) return false;
  }
  return true;
};

// const reverseArr = arr.map(number => {
//   let digit = 0;
//   let res = 0;
//   while (number !== 0) {
//     digit = number % 10;
//     res = res * 10 + digit;
//     number = parseInt(number / 10);
//   }
//   return res;
// });

const reverseArr = arr.map(number => Number(number.toString().split('').reverse().join('')));

const answer = reverseArr.reduce((answer, number) => {
  if (isPrime(number)) answer.push(number);
  return answer;
}, []);

console.log(answer);
