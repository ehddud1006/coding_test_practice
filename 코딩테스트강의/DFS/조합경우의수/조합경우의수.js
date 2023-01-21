const dy = Array.from(Array(5 + 1), () => Array(3 + 1).fill(0));

function dfs(n, r) {
  if (dy[n][r] > 0) return dy[n][r];
  if (n === r || r === 0) return 1;
  return (dy[n][r] = dfs(n - 1, r - 1) + dfs(n - 1, r));
}

console.log(dfs(5, 3));
