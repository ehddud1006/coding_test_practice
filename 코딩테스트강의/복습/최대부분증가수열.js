const N = 8;
const arr = [5, 3, 7, 8, 6, 2, 9, 4];
const dp = Array.from({ length: N + 1 }, () => 1);
let answer = Number.MIN_SAFE_INTEGER;

for (let i = 1; i < arr.length; i++) {
  let max = Number.MIN_SAFE_INTEGER;
  for (let j = i; j >= 0; j--) {
    if (arr[i] > arr[j]) {
      max = Math.max(dp[j], max);
    }
  }
  dp[i] = max + 1;
  answer = Math.max(max + 1, answer);
}

console.log(answer);
