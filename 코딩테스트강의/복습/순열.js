const arr = [1, 2, 3, 4, 5];

const tmp = [];
const visit = Array.from({ length: arr.length + 1 }, () => false);

const dfs = L => {
  if (L === 2) {
    console.log(tmp);
    return;
  }
  for (let i = 0; i < arr.length; i++) {
    if (!visit[i]) {
      visit[i] = true;
      tmp.push(arr[i]);
      dfs(L + 1);
      tmp.pop();
      visit[i] = false;
    }
  }
};

dfs(0);
