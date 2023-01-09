const N = 5;
const M = 5;
const arr = [1, 3, 1, 2, 3];

let lp = 0;
let rp = 0;
let sum = arr[0];
let count = 0;
while (rp < arr.length) {
  if (sum <= M) {
    console.log('sum', sum);
    count += rp - lp + 1;
    sum += arr[++rp];
  } else {
    sum -= arr[lp++];
  }
}

console.log('count', count);
