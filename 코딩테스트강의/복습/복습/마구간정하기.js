const [N, M] = [5, 3];

const arr = [1, 2, 8, 4, 9];

arr.sort((a, b) => a - b);

let [lt, rt] = [1, arr.at(-1)];
let mid = parseInt((lt + rt) / 2);

const test = mid => {
  let ep = arr[0];
  let count = 1;
  arr.forEach(el => {
    if (ep + mid <= el) {
      ep = el;
      count++;
    }
  });
  return count;
};

let answer = 0;
while (lt <= rt) {
  mid = parseInt((lt + rt) / 2);
  let count = test(mid);
  console.log('mid', mid, 'count', count);
  if (count < 3) {
    rt = mid - 1;
  } else {
    if (count === 3) answer = Math.max(answer, mid);
    lt = mid + 1;
  }
}

console.log(answer);
