const N = 5;
const arr = [
  [1, 4],
  [2, 3],
  [3, 5],
  [4, 6],
  [5, 7],
];

arr.sort((a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];
  return a[1] - b[1];
});

const process = [];

for (let [start, end] of arr) {
  process.push([start, 's']);
  process.push([end, 'e']);
}

let time = 0;
let count = 0;
let flag = false;

process.forEach(element => {
  if (element[0] >= time && element[1] === 's') flag = true;
  if (flag && element[1] === 'e') {
    time = element[0];
    count++;
    flag = false;
  }
});

console.log(count);
