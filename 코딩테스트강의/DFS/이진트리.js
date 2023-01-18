function dfs(n) {
  if (n > 7) return;
  console.log(n);
  dfs(2 * n);
  dfs(2 * n + 1);
}

dfs(1);
