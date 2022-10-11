const fs = require("fs");

BOJkey = true;

console.time("code_measure");

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/10828/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

const len = input.shift();
let stack = [];
let result = [];

input.forEach((item, index) => {
  let arr = item.split(" ");
  switch (arr[0]) {
    case "push":
      stack.push(arr[1]);
      break;
    case "pop":
      if (stack.length == 0) {
        result.push("-1");
      } else {
        result.push(stack.pop());
      }
      break;
    case "size":
      result.push(stack.length);
      break;
    case "empty":
      if (stack.length == 0) {
        result.push("1");
      } else {
        result.push("0");
      }
      break;
    case "top":
      if (stack.length == 0) {
        result.push("-1");
      } else {
        result.push(stack[stack.length - 1]);
      }
      break;
  }
});

console.log(result.join("\n"));
