const N = 10;
const K = 3;
const arr = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42];
const sumArr = [];
// for (let i = 0; i < N; i++) {
//   for (let j = 0; j < N; j++) {
//     if (j === i) continue;
//     for (let k = 0; k < N; k++) {
//       if (i === k || j === k) continue;
//       sumArr.push(arr[i] + arr[j] + arr[k]);
//     }
//   }
// }

for (let i = 0; i < N; i++) {
  for (let j = i + 1; j < N; j++) {
    for (let k = j + 1; k < N; k++) {
      sumArr.push(arr[i] + arr[j] + arr[k]);
    }
  }
}
const set = new Set(sumArr);

const uniqueArr = [...set].sort((a, b) => b - a);

console.log(uniqueArr[2]);
