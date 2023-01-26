const N = 3;
const coin = [1, 2, 5];
const target = 15;
const dp = Array.from({ length: target + 1 }, () => Number.MAX_SAFE_INTEGER);
dp[0] = 0;

for (let i = 0; i < N; i++) {
  for (let j = coin[i]; j <= 15; j++) {
    dp[j] = Math.min(dp[j], dp[j - coin[i]] + 1);
  }
}

console.log(dp);
