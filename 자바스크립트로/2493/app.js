const fs = require("fs");

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/2493/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let num = input[0];
let tower = input[1].split(" ");
tower = tower.map((v) => +v);
let stack = [];
let result = [];
// tower 배열에 unshift(0)를 해주어서 index가 동일해지도록 하였다.
tower.unshift(0);
// console.log(tower);

for (let i = 1; i <= num; i++) {
  if (stack.length == 0) {
    stack.push([i, tower[i]]);
  } else if (stack[stack.length - 1][1] < tower[i]) {
    while (stack.length > 0 && stack[stack.length - 1][1] < tower[i]) {
      stack.pop();
    }
    stack.push([i, tower[i]]);
  } else {
    stack.push([i, tower[i]]);
  }

  if (stack.length == 1) result.push(0);
  else result.push(stack[stack.length - 2][0]);
}

console.log(result.join(" "));
