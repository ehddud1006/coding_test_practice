const fs = require("fs");

BOJkey = 1;

const [num, skip] = fs
  .readFileSync(BOJkey ? "./자바스크립트로/1158/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split(" ");

let board = [];
let printer = "<";
let pointer = 0;

for (let i = 1; i < num; i++) {
  board.push({ current: i, next: i + 1 });
}
board.push({ current: 7, next: 1 });
clg;

printer = printer.slice(0, -2) + ">";
console.log(printer);
