const fs = require("fs");

BOJkey = 0;

let input = fs
  .readFileSync(BOJkey ? "./자바스크립트로/2753/input.txt" : "./dev/stdin")
  .toString()
  .trim();

input = +input;
if (input % 4 === 0 && (input % 100 !== 0 || input % 400 === 0)) console.log(1);
else console.log(0);
// if (input % 4 === 0) {
//   if (input % 100 === 0) {
//     if (input % 400 === 0) {
//       console.log(1);
//     } else {
//       console.log(0);
//     }
//   } else {
//     console.log(1);
//   }
// } else {
//   console.log(0);
// }
// const check = (input) => {
//   if (input % 4 !== 0) {
//     return 0;
//   }
//   if (input % 100 !== 0) {
//     return 1;
//   }
//   if (input % 400 !== 0) {
//     return 0;
//   }
//   return 1;
// };

// console.log(check(input));
