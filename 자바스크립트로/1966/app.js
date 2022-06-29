const fs = require("fs");

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/1966/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

let testCaseNumber = input.shift();
let num = 0;
let findIndex = 0;
let arr = [];
let count;
let target;
let ans = 0;
let result = "";
for (let i = 0; i < testCaseNumber; i++) {
  count = 0;
  test = input
    .shift()
    .split(" ")
    .map((v) => +v);
  num = test[0];
  findIndex = test[1];
  priority = input
    .shift()
    .split(" ")
    .map((v) => +v);
  for (let j = 0; j < num; j++) {
    arr.push([j, priority[j]]);
  }
  priority.sort((a, b) => b - a);
  priority.map((el) => {
    while (true) {
      target = arr.shift();
      if (el == target[1]) {
        count++;
        if (findIndex == target[0]) ans = count;
        break;
      } else arr.push(target);
    }
  });
  result += `${ans}\n`;
}

console.log(result);
