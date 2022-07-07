const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./코딩테스트강의/섹션8/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

let [n, m] = input[0];
let arr = input[1];
let temp = Array.from(Array(m), () => 0);
let visit = Array.from(Array(n), () => false);
let result = "";

const dfs = (L) => {
  if (L == m) {
    result = "";
    for (let i = 0; i < m; i++) {
      result += `${temp[i]} `;
    }
    console.log(result);
  } else {
    for (let i = 0; i < n; i++) {
      if (!visit[i]) {
        visit[i] = true;
        temp[L] = arr[i];
        dfs(L + 1);
        visit[i] = false;
      }
    }
  }
};

dfs(0);
