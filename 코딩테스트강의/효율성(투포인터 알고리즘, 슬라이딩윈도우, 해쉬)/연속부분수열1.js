const N = 5;
const M = 6;
const arr = [1, 1, 1, 2, 4];
let lp = 0;
let rp = 0;
let sum = 0;
let count = 0;
while (rp <= N) {
  if (sum === M) {
    count++;
    sum += arr[rp++];
  } else if (sum < M) sum += arr[rp++];
  else sum -= arr[lp++];
}

console.log(count);
