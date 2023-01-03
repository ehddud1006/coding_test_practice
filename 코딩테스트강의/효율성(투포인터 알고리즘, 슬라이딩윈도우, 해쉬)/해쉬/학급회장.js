let N = 15;
let S = 'BACBACCACCBDEDE';
let arr = S.split('');
let answerMap = new Map();

arr.forEach(alphabet => {
  answerMap.set(alphabet, answerMap.get(alphabet) + 1 || 1);
});

const mapToArray = [...answerMap];
mapToArray.sort((a, b) => b[1] - a[1]); // value값 기준 내림차순정렬

console.log(mapToArray[0][0]);
