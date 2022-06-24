const fs = require("fs");

BOJkey = 1;

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/1543/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

const strr = input[1];
let regex = new RegExp(`${strr}`, "g");

let a = input[0].match(regex);
try {
  console.log(a.length);
} catch {
  console.log(0);
}
