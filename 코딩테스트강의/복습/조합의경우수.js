const [N, R] = [33, 19];
const dp = Array.from(Array(N + 1), () => Array(R + 1).fill(-1));

const combination = (n, r) => {
  if (dp[n][r] > 0) return dp[n][r];
  if (n === r || r === 0) return 1;
  return (dp[n][r] = combination(n - 1, r - 1) + combination(n - 1, r));
};

console.log(combination(33, 19));
