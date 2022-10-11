const fs = require("fs");

BOJkey = true;

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/1013/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");
let num = input[0];

let regex = new RegExp(`^(100+1+|01)+$`, "g");
console.log(regex);
let result = [];
for (let i = 1; i <= num; i++) {
  console.log(regex.test(input[i]));
}

console.log(result.join("\n"));
