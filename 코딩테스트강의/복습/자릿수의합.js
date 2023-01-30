const N = 7;
const input = [128, 460, 603, 521, 137, 123];

let max = Number.MIN_SAFE_INTEGER;
const queue = [];

input.forEach(element => {
  let [mok, na] = [element, 0];
  let result = 0;
  while (mok !== 0) {
    na = mok % 10;
    result += na;
    mok = parseInt(mok / 10);
  }
  if (max <= result) {
    queue.push([element, result]);
    max = result;
  }
});

queue.sort((a, b) => {
  if (b[1] === a[1]) return b[0] - a[0];
  return b[1] - a[1];
});

console.log(queue[0][0]);
