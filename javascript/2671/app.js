const fs = require("fs");

BOJkey = true;

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/2671/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let regex = new RegExp(`^(100+1+|01)+$`, "g");

if (regex.test(input[0])) console.log("SUBMARINE");
else console.log("NOISE");
