const str1 = 'teachermode';
const str2 = 'e';

const indexArr = [];

const answer = Array.from({ length: str1.length }, () => Number.MAX_SAFE_INTEGER);
let index = 0;
for (const char of str1) {
  if (char === str2) indexArr.push(index);
  index++;
}

indexArr.forEach(index => {
  str1.split('').forEach((_, i) => {
    if (Math.abs(index - i) < answer[i]) answer[i] = Math.abs(index - i);
  });
});

console.log(answer);
