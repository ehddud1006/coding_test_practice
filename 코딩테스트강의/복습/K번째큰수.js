const N = 10;
const K = 3;
const arr = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42];

const test = [1, 2, 3, 4, 5];
const visit = Array.from({ length: test.length + 1 }, () => false);
const temp = [];
const answer = [];

const dfs = L => {
  if (L === 3) {
    console.log(temp);
    return;
  }
  for (let i = 0; i < test.length; i++) {
    if (!visit[i]) {
      visit[i] = true;
      temp.push(test[i]);
      dfs(L + 1);
      visit[i] = false;
      temp.pop();
    }
  }
};

dfs(0);
