const N = 5;
const arr = [
  [14, 18],
  [12, 15],
  [15, 20],
  [20, 30],
  [5, 14],
];

const process = [];

for (let [start, end] of arr) {
  process.push([start, 's']);
  process.push([end, 'e']);
}

process.sort((a, b) => {
  if (a[0] === b[0]) return a[1].charCodeAt() - b[1].charCodeAt();
  return a[0] - b[0];
});

let peopleCount = 0;
let answer = Number.MIN_SAFE_INTEGER;
for (let [time, type] of process) {
  if (type === 's') peopleCount++;
  else peopleCount--;

  answer = Math.max(peopleCount, answer);
}

console.log(answer);
