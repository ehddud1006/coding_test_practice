const fs = require("fs");

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/1874/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");
let result = [];
let n = input[0];
let stack = [];
let count = 0;
for (let i = 1; i <= n; i++) {
  while (true) {
    if (count > n) break;
    if (stack.length > 0 && stack[stack.length - 1] === +input[i]) {
      stack.pop();
      result.push("-");
      break;
    } else {
      count++;
      stack.push(count);
      result.push("+");
    }
  }
}
if (count > n) console.log("NO");
else console.log(result.join("\n"));
