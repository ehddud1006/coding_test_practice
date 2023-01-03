const fs = require('fs');

BOJkey = false;

const input = fs
  .readFileSync(
    BOJkey ? './코딩테스트강의/효율성(투포인터 알고리즘, 슬라이딩윈도우, 해쉬)/게으른백곰/input.txt' : './dev/stdin',
  )
  .toString()
  .trim()
  .split('\n');

const [N, K] = input.shift().split(' ').map(Number);
const arr = Array.from({ length: 1_000_000 }, () => 0);
const findRange = 2 * K + 1;
let xMax = 0;
let sum = 0;
for (let i = 0; i < N; i++) {
  const [ice, x] = input[i].split(' ').map(Number);
  xMax = Math.max(x, xMax);
  arr[x] = ice;
}

for (let i = 0; i < Math.min(findRange, 1_000_000); i++) {
  sum += arr[i];
}
let answer = sum;
for (let i = findRange; i <= xMax; i++) {
  sum += arr[i] - arr[i - findRange];
  answer = Math.max(answer, sum);
}

console.log(answer);
