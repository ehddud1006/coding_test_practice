N = 11;
answer = '';
const dfs = N => {
  if (N === 0) return;

  dfs(parseInt(N / 2));
  answer += String(N % 2);
};

dfs(N);
console.log(answer);
