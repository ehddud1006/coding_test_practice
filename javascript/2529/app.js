const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/2529/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .reverse();

const N = Number(input.pop());
const inequalitySign = input.pop().split(' ');
const temp = [];
const visited = Array.from({ length: 10 }, () => false);
const expactAnswer = [];
let count = 0;
const dfs = L => {
  // if (L === N + 1) {
  //   for (let i = 0; i < N; i++) {
  //     const target = inequalitySign[i];
  //     switch (target) {
  //       case '<':
  //         if (temp[i] > temp[i + 1]) return;
  //         break;
  //       case '>':
  //         if (temp[i] < temp[i + 1]) return;
  //         break;
  //     }
  //   }
  //   expactAnswer.push(Number(temp.join('')));
  //   return;
  // }
  if (L > N) {
    return;
  }

  for (let i = 0; i < 10; i++) {
    count++;
    // dfs(L + 1);

    if (visited[i]) continue;
    visited[i] = true;
    temp.push(i);
    dfs(L + 1);
    temp.pop();
    visited[i] = false;
  }
};

dfs(0);

// expactAnswer.sort((a, b) => a - b);

// console.log(expactAnswer.at(-1));
// console.log(expactAnswer[0].toString().padStart(N + 1, '0'));
console.log(count);
