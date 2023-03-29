const fs = require('fs');

BOJkey = true;

let [N, word] = fs
  .readFileSync(BOJkey ? './javascript/2529/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.trim());

N = +N;
word = word.split(' ');
const result = [];
const visit = new Array(10).fill(0);
let count = 0;
const dfs = (dep, now) => {
  //   if (dep > 1) {
  //     switch (word[dep - 2]) {
  //       case '>':
  //         if (now[dep - 2] < now[dep - 1]) return;
  //         break;
  //       case '<':
  //         if (now[dep - 2] > now[dep - 1]) return;
  //         break;
  //     }
  //   }
  if (dep > N) {
    // result.push(now);
    return;
  }
  for (let i = 0; i < 10; i++) {
    count++;
    if (visit[i]) continue;
    visit[i] = 1;
    dfs(dep + 1, now + i);
    visit[i] = 0;
  }
};

dfs(0, '');
// let maxx = Math.max(...result);
// let minn = Math.min(...result);
// minn = minn.toString().length < N + 1 ? '0' + minn : minn;

// console.log(maxx, minn);
console.log(count);
