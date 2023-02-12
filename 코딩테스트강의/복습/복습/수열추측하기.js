const N = 4;
const M = 16;

const visited = Array.from({ length: N + 1 }, () => false);
const tmp = [];

const dp = Array.from(Array(N + 1), () => Array(N + 1).fill(0));
let answer = [];
let flag = false;

function combination(n, r) {
  if (dp[n][r] > 0) return dp[n][r];

  if (n === r || r === 0) return 1;

  return (dp[n][r] = combination(n - 1, r) + combination(n - 1, r - 1));
}

function dfs(L) {
  if (flag) return;

  if (L === N) {
    const sum = tmp.reduce((acc, cur, index) => {
      return (acc += cur * combination(N - 1, index));
    }, 0);

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
      dfs(L + 1);
      visited[i] = false;
      tmp.pop();
    }
  }
}

dfs(0);

console.log(answer);
