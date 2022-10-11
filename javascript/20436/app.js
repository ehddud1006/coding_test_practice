const fs = require("fs");

BOJkey = 1;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/20436/input.txt" : "./dev/stdin")
  .toString()
  .trim()
  .split("\n");

// console.log(input);
let keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
let ja = "qwertasdfgzxcv";
let key;
let [left, right] = input[0].split(" ");

const returnXY = (key) => {
  let x, y;
  for (let i = 0; i < 3; i++) {
    y = keyboard[i].indexOf(key);
    if (y !== -1) {
      x = i;
      break;
    }
  }
  return [x, y];
};

let key_x, key_y;
let result = 0;
for (let i = 0; i < input[1].length; i++) {
  key = input[1][i];

  if (ja.includes(key)) {
    [key_x, key_y] = returnXY(key);
    [left_x, left_y] = returnXY(left);
    result += Math.abs(key_x - left_x) + Math.abs(key_y - left_y) + 1;
    left = key;
  } else {
    [key_x, key_y] = returnXY(key);
    [right_x, right_y] = returnXY(right);
    result += Math.abs(key_x - right_x) + Math.abs(key_y - right_y) + 1;
    right = key;
  }
}

console.log(result);
