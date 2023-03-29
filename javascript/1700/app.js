const fs = require('fs');

BOJkey = true;

const input = fs
  .readFileSync(BOJkey ? './javascript/1700/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(el => el.split(' ').map(Number));

const [N, K] = input.shift();
const data = input.pop();
let count = 0;
const multitap = Array.from({ length: N }, () => 0);

data.forEach((electricalAppliance, electricalApplianceIndex) => {
  let [hasEmptySpace, emptySpaceIndex] = [false, 0];

  multitap.forEach((appliance, index) => {
    if (appliance === 0 && multitap.indexOf(electricalAppliance) === -1) {
      hasEmptySpace = true;
      emptySpaceIndex = index;
    }
  });

  if (hasEmptySpace) {
    multitap[emptySpaceIndex] = electricalAppliance;
  }

  if (!hasEmptySpace) {
    if (multitap.indexOf(electricalAppliance) !== -1) return;

    let [order, changeMultitapIndex] = [Number.MIN_SAFE_INTEGER, -1];

    multitap.forEach((appliance, index) => {
      let temp = Number.MAX_SAFE_INTEGER;
      for (let i = electricalApplianceIndex + 1; i < data.length; i++) {
        if (appliance === data[i]) {
          temp = i;
          break;
        }
      }

      if (temp > order) {
        order = temp;
        changeMultitapIndex = index;
      }
    });

    multitap[changeMultitapIndex] = electricalAppliance;
    count++;
  }
});

console.log(count);
