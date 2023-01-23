const N = 4;
const M = 2;
const arr = Array.from({ length: M }, () => 0);

function dfs(L, S) {
  if (S === M) {
    console.log(arr.join(' '));
    return;
  }

  for (let i = L; i <= N; i++) {
    arr[S] = i;
    dfs(i + 1, S + 1);
  }
}

dfs(1, 0);
