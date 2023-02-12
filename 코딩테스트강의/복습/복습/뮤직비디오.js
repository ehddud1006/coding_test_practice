const [N, K] = [9, 3];
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let [lt, rt] = [1, 10_000_000];
let mid = parseInt((lt + rt) / 2);

function recordVideo(time) {
  let sum = 0;
  let count = 1;
  arr.forEach(el => {
    if (sum + el > time) {
      sum = el;
      count++;
    } else sum += el;
  });

  return count;
}
let answer = 0;
while (lt <= rt) {
  mid = parseInt((lt + rt) / 2);

  let count = recordVideo(mid);
  if (count <= 3) {
    if (count === 3) answer = mid;
    rt = mid - 1;
  } else lt = mid + 1;
}

console.log(answer);
