const N = 7;
const input = [126, 460, 603, 521, 137, 123];

let max = 0;
let answer = [];
input.forEach(number => {
  for (const digit of String(number)) {
    // 이것외에 두가지 방법으로 같은 기능을 할 수 있다. 2가지 기능이 뭘까?
    sum += Number(digit);
  }
  console.log(`max:${max} sum:${sum}`);
  if (max < sum) {
    max = sum;
    answer = [];
    answer.push(number);
  } else if (max === sum) answer.push(number);
});

answer.sort((a, b) => a - b);
console.log(answer[0]);

// 1.
// let tmp = number;
// while (tmp !== 0) {
//     sum += tmp % 10;
//     tmp = Math.floor(tmp / 10);
//   }

// 2.
// let sum = String(number)
// .split('')
// .reduce((a, b) => a + Number(b), 0);
