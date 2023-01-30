const N = 5;
const M = 28;

const arr = [
  [6, 6],
  [2, 2],
  [4, 3],
  [4, 5],
  [10, 3],
];

arr.sort((a, b) => a[0] + a[1] - (b[0] + b[1]));

let answer = Number.MIN_SAFE_INTEGER;
for (let i = 0; i < N; i++) {
  let selectStudent = i;
  let budget = M - (arr[selectStudent][0] / 2 + arr[selectStudent][1]);
  let count = 1;
  for (let j = 0; j < N; j++) {
    if (j !== selectStudent && budget - (arr[j][0] + arr[j][1]) >= 0) {
      budget -= arr[j][0] + arr[j][1];
      count++;
    }
  }
  answer = Math.max(count, answer);
}

console.log(answer);
