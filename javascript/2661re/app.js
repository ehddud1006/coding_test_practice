const fs = require('fs');

BOJkey = true;

const input = fs
  .readFileSync(BOJkey ? './javascript/2661re/input.txt' : './dev/stdin')
  .toString()
  .trim();

const N = Number(input);
const temp = [];
let flag = false;

const dfs = L => {
  if (flag) return;

  const str = temp.join('');

  if (str !== '') {
    const half = parseInt(L / 2);

    for (let i = 1; i <= half; i++) {
      if (str.slice(-i * 2, -i) === str.slice(-i)) return;
    }
  }

  if (L === N) {
    console.log(temp.join(''));
    flag = true;
    return;
  }

  temp.push('1');
  dfs(L + 1);
  temp.pop();

  temp.push('2');
  dfs(L + 1);
  temp.pop();

  temp.push('3');
  dfs(L + 1);
  temp.pop();
};

dfs(0);
