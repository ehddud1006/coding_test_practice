const N = 5;
const arr = [
  [1, 4],
  [2, 3],
  [3, 5],
  [4, 6],
  [5, 7],
];
let count = 1;
arr.sort((a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];
  return a[1] - b[1];
});

let [start, end] = arr.shift();
// while (arr.length) {
//   const [nextStart, nextEnd] = arr.shift();
//   if (end <= nextStart) {
//     count++;
//     end = nextEnd;
//   }
// }

for (let x of arr) {
  if (x[0] >= end) {
    count++;
    end = x[1];
  }
}

console.log(count);
