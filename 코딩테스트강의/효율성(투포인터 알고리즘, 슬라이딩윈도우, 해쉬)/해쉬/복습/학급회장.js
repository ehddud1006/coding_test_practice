const N = 15;

const string = 'BACBACCACCBDEDE';
const charMap = new Map();

for (const char of string) {
  charMap.set(char, charMap.get(char) + 1 || 1);
}

const mapToArray = [...charMap];
mapToArray.sort((a, b) => b[1] - a[1]); // value값 기준 내림차순정렬

console.log(mapToArray[0][0]);
