const arr1 = [1, 3, 9, 5, 2];
const arr2 = [3, 2, 5, 7, 8];

arr1.sort();
arr2.sort();

let [lt, rt] = [0, 0];
const answer = [];

while (lt < arr1.length && rt < arr2.length) {
  if (arr1[lt] === arr2[rt]) {
    answer.push(arr1[lt++]);
    rt++;
  } else if (arr1[lt] < arr2[rt]) lt++;
  else rt++;
}

console.log(answer);
