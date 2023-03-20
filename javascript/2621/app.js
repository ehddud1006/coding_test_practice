const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/2621/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const colorMap = { R: 0, B: 0, Y: 0, G: 0 };
const digitMap = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 };
const numberTemp = [];
let answer = Number.MIN_SAFE_INTEGER;
input = input.map(element => [element.split(' ')[0], Number(element.split(' ')[1])]);
input.sort((a, b) => a[1] - b[1]);

const checkSequence = () => {
  sum = 0;
  for (let i = 0; i < 4; i++) {
    sum += input[i + 1][1] - input[i][1];
  }

  if (sum === 4) return true;

  return false;
};

const checkAllColorSame = () => {
  for (let value of Object.values(colorMap)) {
    if (value === 5) return true;
  }

  return false;
};

for (let [color, digit] of input) {
  colorMap[color] += 1;
  digitMap[digit] += 1;
}

for (let [number, value] of Object.entries(digitMap)) {
  numberTemp.push([number, value]);
}
numberTemp.sort((a, b) => b[1] - a[1]);

const numberString = numberTemp.reduce((acc, cur) => {
  if (cur[1] >= 1) return acc + cur[1].toString();

  return acc;
}, '');

// 1
if (checkAllColorSame() && checkSequence()) {
  let max = Number.MIN_SAFE_INTEGER;

  for (let [number, value] of Object.entries(digitMap)) {
    max = Math.max(max, Number(number));
  }

  answer = Math.max(900 + max, answer);
}

// 2
if (numberString === '41') {
  let target = 0;
  for (let [number, value] of Object.entries(digitMap)) {
    if (value === 4) target = Number(number);
  }

  answer = Math.max(800 + target, answer);
}

// 3
if (numberString === '32') {
  let threeEqualNumber = 0;
  let twoEqualNumber = 0;
  for (let [number, value] of Object.entries(digitMap)) {
    if (value === 3) threeEqualNumber = Number(number);
    if (value === 2) twoEqualNumber = Number(number);
  }

  answer = Math.max(threeEqualNumber * 10 + twoEqualNumber + 700, answer);
}

// 4
if (checkAllColorSame()) {
  let max = Number.MIN_SAFE_INTEGER;

  for (let [number, value] of Object.entries(digitMap)) {
    if (value > 0) max = Math.max(max, Number(number));
  }
  answer = Math.max(600 + max, answer);
}

// 5
if (checkSequence()) {
  let max = Number.MIN_SAFE_INTEGER;

  for (let [number, value] of Object.entries(digitMap)) {
    if (value > 0) max = Math.max(max, Number(number));
  }

  answer = Math.max(500 + max, answer);
}

// 6
if (numberString === '311') {
  let threeEqualNumber = 0;

  for (let [number, value] of Object.entries(digitMap)) {
    if (value === 3) threeEqualNumber = Number(number);
  }

  answer = Math.max(threeEqualNumber + 400, answer);
}

// 7
if (numberString === '221') {
  const twoEqualNumber = [];

  for (let [number, value] of Object.entries(digitMap)) {
    if (value === 2) twoEqualNumber.push(Number(number));
  }

  twoEqualNumber.sort((a, b) => b - a);
  answer = Math.max(twoEqualNumber[0] * 10 + twoEqualNumber[1] + 300, answer);
}

// 8
if (numberString === '2111') {
  let twoEqualNumber = 0;

  for (let [number, value] of Object.entries(digitMap)) {
    if (value === 2) twoEqualNumber = Number(number);
  }

  answer = Math.max(twoEqualNumber + 200, answer);
}

// 9
let target = 0;

for (let [number, value] of Object.entries(digitMap)) {
  if (value > 0) target = Math.max(target, Number(number));
}

answer = Math.max(target + 100, answer);

console.log(answer);
