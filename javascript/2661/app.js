const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/2661/input.txt' : './dev/stdin')
  .toString()
  .trim();

const N = Number(input);
let flag = false;

const checkDuplicate = str => {
  const len = str.length;
  const searchRange = parseInt(len / 2, 10);

  for (let i = 1; i <= searchRange; i++) {
    if (str.slice(len - i, len) === str.slice(len - 2 * i, len - i)) return true;
  }

  return false;
};

const dfs = (L, str) => {
  if (flag) return;

  if (checkDuplicate(str)) return;

  if (L === N) {
    console.log(str);
    flag = true;
    return;
  }

  dfs(L + 1, str + '1');
  dfs(L + 1, str + '2');
  dfs(L + 1, str + '3');
};

dfs(0, '');
