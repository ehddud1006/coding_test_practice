const fs = require('fs');

BOJkey = true;

const input = fs
  .readFileSync(BOJkey ? './javascript/1700re/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, K] = input.shift().split(' ').map(Number);
const data = input.shift().split(' ');
const plug = [];
let count = 0;

data.every((item, index) => {
  if (plug.length < N) plug.push(item);

  if (plug.length === N) {
    if (plug.includes(item)) return true;
    else {
      let [order, changeMultitapIndex] = [Number.MIN_SAFE_INTEGER, -1];

      plug.forEach((appliance, idx) => {
        let temp = Number.MAX_SAFE_INTEGER;
        for (let i = index + 1; i < data.length; i++) {
          if (appliance === data[i]) {
            temp = i;
            break;
          }
        }

        if (temp > order) {
          order = temp;
          changeMultitapIndex = idx;
        }
      });

      plug[changeMultitapIndex] = item;
      count++;
    }
  }

  return true;
});

console.log(count);
