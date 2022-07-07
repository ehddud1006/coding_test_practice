// 완전탐색으로 풀어야할까

// 아 이게 중복순열이구나
// 3
// 1 2 5
// 동전을 중복해서 뽑는다는 것이니까
// 지렸다
// 그러면 아까 배웠던 로직을 응용하면 될것같은데

const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./코딩테스트강의/섹션8/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

console.log(input);
let coinNumber = input[0][0];
let cointKind = input[1];
let limit = input[2][0];
let minn = Number.MAX_SAFE_INTEGER;
const dfs = (L, S) => {
  if (S > limit) return;
  if (L >= answer) return;
  if (S === limit) {
    minn = Math.min(minn, L);
  } else {
    for (let i = 0; i < coinNumber; i++) {
      dfs(L + 1, S + cointKind[i]);
    }
  }
};

dfs(0, 0);
console.log(minn);
