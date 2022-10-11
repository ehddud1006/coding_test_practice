const fs = require("fs");

BOJkey = true;

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/1264/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let regex = new RegExp(`[aeiou]`, "ig");
let result = [];
for (let i = 0; i < input.length - 1; i++) {
  let a = input[i].match(regex);
  try {
    result.push(a.length);
  } catch {
    result.push(0);
  }
}
console.log(result.join("\n"));
