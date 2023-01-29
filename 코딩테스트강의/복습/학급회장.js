let N = 15;
let S = 'BACBACCACCBDEDE';

const mp = new Map();

for (x of S) {
  mp.set(x, mp.get(x) + 1 || 1);
}

const mapToArray = [...mp];
mapToArray.sort((a, b) => b[1] - a[1]);
console.log(mapToArray[0][0]);
