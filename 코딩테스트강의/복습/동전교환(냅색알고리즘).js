const N = 3;
const coins = [1, 2, 5];
const M = 15;

const dp = Array.from({ length: M + 1 }, () => Number.MAX_SAFE_INTEGER);
dp[0] = 0;
for (let i = 0; i < coins.length; i++) {
  const coin = coins[i];
  for (let j = coin; j <= M; j++) {
    dp[j] = Math.min(dp[j - coin] + 1, dp[j]);
  }
}

console.log(dp[15]);
