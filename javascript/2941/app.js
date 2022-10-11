const fs = require("fs");

BOJkey = true;

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/2941/input.txt" : "./dev/stdin")
  .toString()
  .trim();

const answer = input
  .replace(/c\=/g, "!")
  .replace(/c\-/g, "!")
  .replace(/dz\=/g, "!")
  .replace(/s\=/g, "!")
  .replace(/d\-/g, "!")
  .replace(/lj/g, "!")
  .replace(/nj/g, "!")
  .replace(/z\=/g, "!");
console.log(answer.length);
