const a = [1, 3, 5];
const b = [2, 3, 6, 7, 9];
const answer = [];

let [lt, rt] = [0, 0];

while (lt !== a.length && rt !== b.length) {
  if (a[lt] >= b[rt]) answer.push(b[rt++]);
  else answer.push(a[lt++]);
}

while (lt !== a.length) answer.push(a[lt++]);
while (rt !== b.length) answer.push(b[rt++]);

console.log(answer);
