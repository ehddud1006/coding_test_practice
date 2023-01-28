const [N, T] = [8, 32];
const arr = [23, 87, 65, 12, 57, 32, 99, 81];

arr.sort((a, b) => a - b);

let [lt, rt] = [0, arr.length - 1];
let mid = parseInt((lt + rt) / 2);
let answer = 0;

while (lt <= rt) {
  mid = parseInt((lt + rt) / 2);
  if (arr[mid] === T) {
    answer = mid + 1;
    break;
  } else if (arr[mid] > T) rt = mid - 1;
  else lt = mid + 1;
}

console.log(answer);
