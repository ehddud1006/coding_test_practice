const arr = [87, 89, 92, 100, 76];
const copyArr = [...arr];
copyArr.sort((a, b) => b - a);

const scoreMap = new Map();
const answer = [];

copyArr.forEach((el, index) => {
  scoreMap.set(el, index + 1);
});

arr.forEach(el => {
  answer.push(scoreMap.get(el));
});

console.log(answer);
