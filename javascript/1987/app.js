const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/1987/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [R, C] = input.shift().split(' ').map(Number);

input = input.map(el => el.split(''));
// const checkDuplicate = [];
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

const checkDuplicate = {
  A: false,
  B: false,
  C: false,
  D: false,
  E: false,
  F: false,
  G: false,
  H: false,
  I: false,
  J: false,
  K: false,
  L: false,
  M: false,
  N: false,
  O: false,
  P: false,
  Q: false,
  R: false,
  S: false,
  T: false,
  U: false,
  V: false,
  W: false,
  X: false,
  Y: false,
  Z: false,
};

let answer = Number.MIN_SAFE_INTEGER;
let count = 0;
let count2 = 0;
const dfs = (x, y, step) => {
  //   if (step < answer) return;
  answer = Math.max(answer, step);
  count += 1;
  for (let i = 0; i < 4; i++) {
    const [nx, ny] = [x + dx[i], y + dy[i]];

    console.time('o');

    if (nx > -1 && nx < R && ny > -1 && ny < C && checkDuplicate[input[nx][ny]] === false) {
    }
    console.timeEnd('o');

    if (nx > -1 && nx < R && ny > -1 && ny < C && checkDuplicate[input[nx][ny]] === false) {
      count2 += 1;
      checkDuplicate[input[nx][ny]] = true;
      dfs(nx, ny, step + 1);
      checkDuplicate[input[nx][ny]] = false;
    }
  }
};

checkDuplicate[input[0][0]] = true;

dfs(0, 0, 1);
console.log(answer);
console.log(count);
console.log(count2);
