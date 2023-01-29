const N = 10;
const K = 3;
const arr = [12, 15, 11, 20, 25, 10, 20, 19, 13, 15];

let [lt, rt] = [0, K - 1];
let sum = 0;
let answer = Number.MIN_SAFE_INTEGER;
for (let i = lt; i <= rt; i++) {
  sum += arr[i];
}

while (rt < arr.length) {
  answer = Math.max(sum, answer);
  sum += arr[++rt];
  sum -= arr[lt++];
}

console.log(answer);
