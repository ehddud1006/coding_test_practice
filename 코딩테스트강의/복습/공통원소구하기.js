const arr1 = [1, 3, 9, 5, 2];
const arr2 = [3, 2, 5, 7, 8];

let [lt, rt] = [0, 0];

const answer = [];

arr1.sort();
arr2.sort();

while (lt !== arr1.length && rt !== arr2.length) {
  console.log(arr1[lt]);
  if (arr1[lt] < arr2[rt]) lt++;
  else if (arr1[lt] > arr2[rt]) rt++;
  else {
    answer.push(arr1[lt++]);
    rt++;
  }
}

console.log(answer);
