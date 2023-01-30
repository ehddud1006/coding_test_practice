const arr = [1, 2, 3, 4, 5];

const tmp = [];
const dfs = L => {
  if (L === 2) {
    console.log(tmp);
    return;
  }
  for (let i = 0; i < arr.length; i++) {
    tmp.push(arr[i]);
    dfs(L + 1);
    tmp.pop();
  }
};

dfs(0);
