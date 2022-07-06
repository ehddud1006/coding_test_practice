input = 6;
arr = [1, 3, 1, 6, 5, 10];
sum = 0;
for (let i = 0; i < input.length; i++) {
  sum += arr[i];
}
flag = false;
const dfs = (L, S) => {
  if (flag) return;
  if (L === input) {
    if (sum - S === S) {
      console.log("YES");
      flag = true;
    }
  } else {
    dfs(L + 1, S + arr[L]);
    dfs(L + 1, S);
  }
};

dfs(0, 0);
