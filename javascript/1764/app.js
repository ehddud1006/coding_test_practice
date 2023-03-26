const fs = require('fs');

BOJkey = true;

let input = fs
  .readFileSync(BOJkey ? './javascript/1764/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const hashMap = {};
let len = 0;
const [N, M] = input.shift().split(' ').map(Number);

for (let i = 0; i < N; i++) {
  hashMap[input[i]] = 1;
}

for (let i = N; i < N + M; i++) {
  if (hashMap[input[i]]) hashMap[input[i]] += 1;
}

const answer = [];
for (let [name, value] of Object.entries(hashMap)) {
  if (value === 2) answer.push(name);
}

answer.sort();

let str = String(answer.length) + '\n';

for (let name of answer) {
  str += name + '\n';
}

console.log(str);
