const arr = [1, 2, 1, 3, 1, 1, 1, 2];

const N = 8;
const M = 6;

let [lt, rt] = [0, 0];
let sum = arr[0];
let count = 0;

while (rt < N) {
  if (sum < M) {
    sum += arr[++rt];
  } else if (sum === M) {
    count++;
    sum += arr[++rt];
  } else {
    sum -= arr[lt++];
  }
}

console.log(count);
