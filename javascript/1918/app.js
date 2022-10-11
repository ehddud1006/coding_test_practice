const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/1918/input.txt" : "./dev/stdin")
  .toString()
  .trim();

let ans = "";
let stack = [];
for (let i = 0; i < input.length; i++) {
  if (input[i].charCodeAt() >= 65 && input[i].charCodeAt() <= 90) {
    ans += input[i];
  } else {
    switch (input[i]) {
      case "(":
        stack.push("(");
        break;
      case "+":
        while (stack.length > 0 && stack[stack.length - 1] != "(") {
          ans += stack.pop();
        }
        stack.push("+");
        break;
      case "-":
        while (stack.length > 0 && stack[stack.length - 1] != "(") {
          ans += stack.pop();
        }
        stack.push("-");
        break;
      case "/":
        while (
          stack.length > 0 &&
          (stack[stack.length - 1] == "/" || stack[stack.length - 1] == "*")
        ) {
          ans += stack.pop();
        }
        stack.push("/");
        break;
      case "*":
        while (
          stack.length > 0 &&
          (stack[stack.length - 1] == "/" || stack[stack.length - 1] == "*")
        ) {
          ans += stack.pop();
        }
        stack.push("*");
        break;
      case ")":
        while (stack.length > 0 && stack[stack.length - 1] != "(") {
          ans += stack.pop();
        }
        stack.pop();
        break;
    }
  }
}
while (stack.length) {
  ans += stack.pop();
}
console.log(ans);
