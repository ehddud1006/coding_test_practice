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
  let money = M;
  money -= arr[i][0] / 2 + arr[i][1];
  let cnt = 1;
  for (let j = 0; j < N; j++) {
    if (i !== j && money < arr[j][0] + arr[j][1]) break;
    if (i !== j && money >= arr[j][0] + arr[j][1]) {
      money -= arr[j][0] + arr[j][1];
      cnt++;
    }
  }
  answer = Math.max(answer, cnt);
}

console.log(answer);
