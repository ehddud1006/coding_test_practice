const fs = require("fs");

BOJkey = true;
if (BOJkey) {
  var input = fs
    .readFileSync("./자바스크립트로/10926/input.txt")
    .toString()
    .trim();
} else {
  var input = fs.readFileSync("./dev/stdin").toString().trim();
}
