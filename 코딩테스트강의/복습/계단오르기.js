const N = 7;
const dp = Array.from({ length: N + 1 }, () => 0);

dp[1] = 1;
dp[2] = 2;
for (let i = 3; i <= N; i++) {
  dp[i] = dp[i - 1] + dp[i - 2];
}

console.log(dp[7]);
