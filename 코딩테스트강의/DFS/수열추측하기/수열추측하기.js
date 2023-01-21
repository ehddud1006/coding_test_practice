const n = 4;
const total = 16;

const dp = Array.from(Array(11), () => Array(11).fill(0));
const visit = Array.from({ length: n + 1 }, () => false);
const permutation = [];
const pascal = [];
let endFlag = false;

for (let i = 0; i < n; i++) {
  pascal.push(combination(n - 1, i));
}

function combination(n, r) {
  if (dp[n][r] > 0) return dp[n][r];
  if (n === r || r === 0) return 1;
  return (dp[n][r] = combination(n - 1, r - 1) + combination(n - 1, r));
}

function dfs(L) {
  if (endFlag) return;
  if (L === n) {
    let sum = 0;
    for (let i = 0; i < n; i++) {
      sum += permutation[i] * pascal[i];
    }
    if (sum === total) {
      endFlag = true;
      console.log(permutation.join(' '));
    }
    return;
  }
  for (let i = 1; i <= n; i++) {
    if (!visit[i]) {
      visit[i] = true;
      permutation.push(i);
      dfs(L + 1);
      visit[i] = false;
      permutation.pop();
    }
  }
}

dfs(0);
