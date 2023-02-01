const N = 4;
const M = 2;

const arr = [2, 4, 5, 8, 12];
const tmp = [];

let count = 0;
const dfs = (L, S) => {
  if (L === 3) {
    let sum = tmp.reduce((acc, cur) => acc + cur, 0);
    if (sum % 6 === 0) count++;
    return;
  }

  for (let i = S; i <= N; i++) {
    tmp.push(arr[i]);
    dfs(L + 1, i + 1);
    tmp.pop();
  }
};

dfs(0, 0);

console.log(count);
