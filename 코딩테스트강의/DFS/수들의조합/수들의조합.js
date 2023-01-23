const arr = [2, 4, 5, 8, 12];
const n = 5;
const k = 3;
const s = 6;

let sum = 0;
let count = 0;
function dfs(L, S) {
  if (S === k) {
    if (sum % s === 0) count++;
    return;
  }
  for (let i = L; i < n; i++) {
    sum += arr[i];
    dfs(i + 1, S + 1);
    sum -= arr[i];
  }
}

dfs(0, 0);
console.log(count);
