const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/3079/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, M] = input.shift().split(' ');

let [left, right] = [1, Math.max(...input) * M];
let answer = Number.MAX_SAFE_INTEGER;

while (left <= right) {
  let mid = parseInt((left + right) / 2);
  let count = 0;

  for (let i = 0; i < N; i++) {
    count += parseInt(mid / input[i]);
  }

  if (count >= M) {
    answer = Math.min(mid, answer);
    right = mid - 1;
  } else left = mid + 1;
}

console.log(answer);
