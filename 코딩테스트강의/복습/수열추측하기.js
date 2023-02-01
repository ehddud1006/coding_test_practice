const tmp = [];
const N = 4;
const M = 16;

const visited = Array.from({ length: N + 1 }, () => false);
const dp = Array.from(Array(N + 1), () => Array(N + 1).fill(0));
const pascal = [];
let answer = [];
let flag = false;
const combination = (n, r) => {
  if (dp[n][r] > 0) return dp[n][r];
  if (n === r || r === 0) return 1;
  return (dp[n][r] = combination(n - 1, r - 1) + combination(n - 1, r));
};

for (let i = 0; i < N; i++) {
  pascal.push(combination(N - 1, i));
}

const dfs = n => {
  if (flag) return;
  if (n === N) {
    let sum = 0;
    for (let k = 0; k < N; k++) {
      sum += pascal[k] * tmp[k];
    }
    if (sum === M) {
      answer = [...tmp];
      flag = true;
    }

    return;
  }
  for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      tmp.push(i);
      dfs(n + 1);
      tmp.pop();
      visited[i] = false;
    }
  }
};

dfs(0);

console.log(answer);
