const fs = require("fs");

BOJkey = true;

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/2738/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((x) =>
    x
      .trim()
      .split(" ")
      .map((x) => +x)
  );
const [n, m] = input.shift();
// let arr = new Array(m);
// let array = [];
// arr.fill(0);
// for (let i = 0; i < n; i++) {
//   array.push([...arr]);
// }
let array = Array.from(Array(n), () => Array(m).fill(0));
// console.log(array);
// console.log(arr);
// console.log(input);
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    array[i][j] = input[i][j] + input[i + n][j];
  }
}

let answer = "";
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    answer += array[i][j].toString() + " ";
  }
  answer += "\n";
}
console.log(answer);
// console.log(input);
