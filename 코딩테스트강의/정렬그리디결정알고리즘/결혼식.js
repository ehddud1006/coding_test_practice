const N = 5;
const arr = [
  [14, 18],
  [12, 15],
  [15, 20],
  [20, 30],
  [5, 14],
];

const T_line = [];

for (let x of arr) {
  T_line.push([x[0], 's']);
  T_line.push([x[1], 'e']);
}

T_line.sort((a, b) => {
  if (a[0] === b[0]) return a[1].charCodeAt() - b[1].charCodeAt();
  else return a[0] - b[0];
});

let count = 0;
let answer = Number.MIN_SAFE_INTEGER;
for (let x of T_line) {
  if (x[1] === 's') count++;
  else count--;
  answer = Math.max(count, answer);
}

console.log(answer);
