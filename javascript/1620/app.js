const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/1620/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [num, problemNum] = input[0].split(" ").map((v) => +v);
let dicName = new Map();
let dicNumber = new Map();
for (let i = 1; i <= num; i++) {
  dicName.set(input[i], i);
  dicNumber.set(i, input[i]);
}

let result = "";

for (let i = num + 1; i <= num + problemNum; i++) {
  if (/[0-9]/.test(input[i])) {
    result += dicNumber.get(+input[i]) + "\n";
  } else {
    result += dicName.get(input[i]) + "\n";
  }
}

console.log(result);
