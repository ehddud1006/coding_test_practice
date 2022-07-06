const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/16719/input.txt" : "./dev/stdin")
  .toString()
  .trim();
let min;
let result = new Array(input.length).fill("");
// console.log(result);
S = input.trim().split("");
count = 1;
const dfs = (arr, start) => {
  let idx;
  if (arr.length == 0) {
    return;
  } else {
    sort_arr = [...arr];
    sort_arr.sort();
    min = sort_arr[0];
    idx = arr.indexOf(min);
    result[start + idx] = min;
    console.log(result.join(""));
    dfs([...arr].slice(idx + 1), start + idx + 1);
    dfs([...arr].slice(0, idx), start);
  }
};

dfs(S, 0);
