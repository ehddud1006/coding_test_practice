const arr = [11, 7, 5, 6, 10, 9];

for (let i = 1; i < arr.length; i++) {
  let temp = arr[i];
  let j = 0;
  for (j = i - 1; j >= 0; j--) {
    if (temp < arr[j]) arr[j + 1] = arr[j];
    else break;
  }
  arr[j + 1] = temp;
}

console.log(arr);
