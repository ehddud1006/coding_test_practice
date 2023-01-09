const N = 10;
const K = 3;

const arr = [12, 15, 11, 20, 25, 10, 20, 19, 13, 15];

let lp = 0;
let rp = K - 1;

let answer = 0;
let sum = 0;
for (let i = 0; i < K; i++) sum += arr[i];

while (rp < N) {
  console.log(answer);
  answer = Math.max(answer, sum);
  sum -= arr[lp++];
  sum += arr[++rp];
}

console.log(answer);
