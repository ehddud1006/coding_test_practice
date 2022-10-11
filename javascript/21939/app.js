const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/10828/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");
