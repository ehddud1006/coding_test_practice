n = 4;
m = 3;
let temp = Array.from(Array(m), () => 0);
console.log(temp);
const dfs = (L) => {
  if (L === m) {
    let answer = "";
    for (let i = 0; i < m; i++) {
      answer += `${temp[i]} `;
    }
    console.log(answer);
  } else {
    for (let i = 1; i <= n; i++) {
      temp[L] = i;
      dfs(L + 1);
    }
  }
};

dfs(0);
