const N = 6;
const arr = [1, 3, 5, 6, 7, 10];

const sum = arr.reduce((acc, cur) => (acc += cur), 0);
let flag = false;
const dfs = (n, s) => {
  if (n >= N) {
    console.log(s);
    if (s === sum - s) flag = true;
    return;
  }
  dfs(n + 1, s + arr[n]);
  dfs(n + 1, s);
};

dfs(0, 0);
if (flag) console.log('YES');
else onsole.log('NO');
