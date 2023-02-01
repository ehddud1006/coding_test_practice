const str1 = 'teachermode';
const str2 = 'e';
const idxArray = Array.from({ length: str1.length }, () => Number.MAX_SAFE_INTEGER);
const targetIdxArray = [];
for (let i = 0; i < str1.length; i++) {
  if (str1[i] === str2) targetIdxArray.push(i);
}

console.log(targetIdxArray);

targetIdxArray.forEach(idx => {
  for (let i = 0; i < str1.length; i++) {
    const gap = Math.abs(i - idx);
    if (gap < idxArray[i]) idxArray[i] = gap;
  }
});

console.log(idxArray);
