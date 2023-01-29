const N = 5;
const M = 5;

const arr = [1, 3, 1, 2, 3];
let [lt, rt] = [0, 0];
let sum = arr[0];
let count = 0;

while (rt < arr.length) {
  if (sum <= M) {
    count += rt - lt + 1;
    sum += arr[++rt];
  } else {
    sum -= arr[lt++];
  }
}

console.log(count);
