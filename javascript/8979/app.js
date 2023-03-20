const fs = require('fs');

BOJkey = true;

let answer = '';
let input = fs
  .readFileSync(BOJkey ? './javascript/8979/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, M] = input.shift().split(' ');
let [prevGold, prevSilver, prevBronze, rank, equal] = [0, 0, 0, 0, 1];

input = input.map(element => element.split(' '));

input.sort((a, b) => {
  if (b[1] === a[1]) {
    if (b[2] === a[2]) return b[3] - a[3];

    return b[2] - a[2];
  }
  return b[1] - a[1];
});

input.forEach(element => {
  let [target, gold, silver, bronze] = element;
  if (gold === prevGold && silver === prevSilver && bronze === prevBronze) {
    equal++;
  } else {
    [prevGold, prevSilver, prevBronze, rank] = [gold, silver, bronze, rank + equal];
    equal = 1;
  }

  if (target === String(M)) console.log(rank);
});
