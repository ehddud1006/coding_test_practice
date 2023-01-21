function dfs(n) {
  if (n === 1) return 1;
  return n * dfs(n - 1);
}

let answer = dfs(5);
console.log(answer);
