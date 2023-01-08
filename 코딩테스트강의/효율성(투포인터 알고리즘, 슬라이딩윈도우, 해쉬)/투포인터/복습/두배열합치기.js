const arr1 = [1, 3, 5];
const arr2 = [2, 3, 6, 7, 9];
let upperP = 0;
let lowerP = 0;
const answer = [];

while (upperP < arr1.length && lowerP < arr2.length) {
  if (arr1[upperP] >= arr2[lowerP]) answer.push(arr2[lowerP++]);
  else answer.push(arr1[upperP++]);
}

while (upperP < arr1.length) answer.push(arr1[upperP++]);
while (lowerP < arr2.length) answer.push(arr2[lowerP++]);

console.log(answer);
