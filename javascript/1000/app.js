const fs = require("fs");
let input = fs.readFileSync("./자바스크립트로/1000/input.txt").toString();

const arr = input.split(" ").map((v) => +v);

console.log(arr[0] + arr[1]);
