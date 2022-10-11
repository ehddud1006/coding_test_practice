const fs = require("fs");

BOJkey = true;

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/2857/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");
let regex = new RegExp(`FBI`);
let result = "";
input.map((el, idx) => {
  if (regex.test(el)) {
    result += `${idx + 1} `;
  }
});
if (result == "") console.log("HE GOT AWAY!");
else console.log(result);
