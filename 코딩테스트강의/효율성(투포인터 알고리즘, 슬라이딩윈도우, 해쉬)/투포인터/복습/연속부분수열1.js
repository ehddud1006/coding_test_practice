const arr = [1, 2, 1, 3, 1, 1, 1, 2];

const N = 8;
const M = 6;

let lp = 0;
let rp = 0;
let sum = arr[0];
let answer = 0;

while (rp < arr.length) {
  if (sum < M) {
    sum += arr[++rp];
  } else if (sum === M) {
    answer++;
    sum += arr[++rp];
  } else {
    sum -= arr[lp++];
  }
}

console.log(answer);
