const fs = require("fs");

BOJkey = true;

var input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/2164/input.txt" : "./dev/stdin")
  .toString()
  .trim();

let cardBox = [...Array(+input + 1).keys()];
let cardBoxStart = 1;

for (let i = 0; i < input - 1; i++) {
  cardBoxStart++;
  cardBox.push(cardBox[cardBoxStart]);
  cardBoxStart++;
}

console.log(cardBox[cardBoxStart]);
