const N = 3;
const tmp = [];

const dfs = n => {
  if (n > N) {
    console.log(tmp.join(' '));
    return;
  }
  tmp.push(n);
  dfs(n + 1);
  tmp.pop();
  dfs(n + 1);
};

dfs(1);
