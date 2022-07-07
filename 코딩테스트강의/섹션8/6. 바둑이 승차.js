const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./코딩테스트강의/섹션8/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let limit = input.shift().split(" ")[0];
console.log(limit);
input = input.map((v) => +v);
let answer = 0;
const dfs = (L, S) => {
  if (L == 5) {
    if (answer < S && S <= limit) answer = S;
    return;
  } else {
    dfs(L + 1, S + input[L]);
    dfs(L + 1, S);
  }
};

dfs(0, 0);
console.log(answer);
console.log(Math.max(5, 3));
