const N = 6;
const arr = [11, 7, 5, 6, 10, 9];

for (let i = 0; i < arr.length; i++) {
  console.log(arr);
  let tmp = arr[i];
  let j = 0;
  for (j = i - 1; j >= 0; j--) {
    if (arr[j] > tmp) arr[j + 1] = arr[j];
    else break;
  }
  arr[j + 1] = tmp;
}

console.log(arr);
