const N = 4;
const M = 2;

// const visited =
const tmp = [];

const dfs = (L, S) => {
  if (L === M) {
    console.log(tmp);
    return;
  }

  for (let i = S; i <= N; i++) {
    tmp.push(i);
    dfs(L + 1, i + 1);
    tmp.pop();
  }
};

dfs(0, 1);
