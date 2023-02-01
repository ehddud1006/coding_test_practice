const N = 5;

const dfs = n => {
  if (n === 1) return 1;
  return n * dfs(n - 1);
};

answer = dfs(5);

console.log(answer);
