const N = 9;
const arr = [120, 125, 152, 130, 135, 135, 143, 127, 160];

const copyArr = [...arr];
copyArr.sort((a, b) => a - b);
const answer = [];

for (let i = 0; i < N; i++) {
  if (arr[i] !== copyArr[i]) answer.push(i + 1);
}

console.log(answer.join(' '));
