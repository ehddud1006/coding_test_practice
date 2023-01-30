const N = 10;
const K = 3;
const arr = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42];

const visit = Array.from({ length: arr.length + 1 }, () => false);
const temp = [];
let answer = [];

const dfs = (L, S) => {
  if (L === 3) {
    const sum = temp.reduce((res, number) => (res += number), 0);
    answer.push(sum);
    return;
  }
  for (let i = S; i < arr.length; i++) {
    if (!visit[i]) {
      visit[i] = true;
      temp.push(arr[i]);
      dfs(L + 1, i + 1);
      visit[i] = false;
      temp.pop();
    }
  }
};

dfs(0, 0);

answer = [...new Set(answer)];
answer.sort((a, b) => b - a);

console.log(answer[K - 1]);
