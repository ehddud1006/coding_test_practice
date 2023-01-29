const input1 = 'AbaAeCe';
const input2 = 'baeeACA';

const mp = new Map();

for (let x of input1) {
  mp.set(x, mp.get(x) + 1 || 1);
}
for (let x of input2) {
  mp.set(x, mp.get(x) - 1 ?? -1);
}

const mapToArray = [...mp];
let flag = true;
for (let [_, value] of mapToArray) {
  if (value < 0) flag = false;
}

console.log(flag ? 'YES' : 'NO');
