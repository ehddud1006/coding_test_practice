const arr1 = [1, 3, 9, 5, 2];
const arr2 = [3, 2, 5, 7, 8];
let upperP = 0;
let lowerP = 0;
const answer = [];

arr1.sort();
arr2.sort();

while (upperP < arr1.length && lowerP < arr2.length) {
  if (arr1[upperP] < arr2[lowerP]) upperP++;
  else if (arr1[upperP] === arr2[lowerP]) {
    answer.push(arr1[upperP++]);
    lowerP++;
  } else lowerP++;
}

console.log(answer);
