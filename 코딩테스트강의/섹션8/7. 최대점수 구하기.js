const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./코딩테스트강의/섹션8/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

let [N, limit] = input.shift();
let answer = 0;
const dfs = (L, point, time) => {
  if (L == N) {
    if (time <= limit) {
      answer = Math.max(answer, point);
    }
    return;
  } else {
    dfs(L + 1, point + input[L][0], time + input[L][1]);
    dfs(L + 1, point, time);
  }
};

dfs(0, 0, 0);
console.log(answer);
