const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/14425/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let number = input[0].split(" ").map((v) => +v);
let S_Number = number[0];
let stringNumber = number[1];

let dic = new Map();
let count = 0;
for (let i = 1; i <= S_Number; i++) {
  dic.set(input[i], true);
}

for (let i = S_Number + 1; i <= input.length; i++) {
  if (dic.get(input[i])) {
    count++;
  }
}

console.log(count);
