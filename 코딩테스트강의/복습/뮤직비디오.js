const [N, K] = [9, 3];
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let answer = Number.MAX_SAFE_INTEGER;
let [lt, rt] = [1, 10_000_000];
let mid = parseInt((lt + rt) / 2);

const record = volume => {
  let sum = 0;
  let count = 1;
  arr.forEach(element => {
    if (sum + element > volume) {
      sum = element;
      count++;
    } else sum += element;
  });
  return count;
};

while (lt <= rt) {
  mid = parseInt((lt + rt) / 2);

  let count = record(mid);
  if (count > K) {
    lt = mid + 1;
  } else {
    if (count === K) answer = Math.min(answer, mid);
    rt = mid - 1;
  }
}

console.log(answer);
