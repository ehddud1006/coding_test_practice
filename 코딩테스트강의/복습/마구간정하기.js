const [N, M] = [5, 3];

const arr = [1, 2, 8, 4, 9];

arr.sort((a, b) => a - b);

let [lt, rt] = [1, arr[arr.length - 1]];
let mid = parseInt((lt + rt) / 2);
let answer = 0;

const placeHorses = dist => {
  let [ep, count] = [1, 1];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] - ep >= dist) {
      ep = arr[i];
      count++;
    }
  }
  return count;
};
while (lt <= rt) {
  mid = parseInt((lt + rt) / 2);
  let placedHorses = placeHorses(mid);
  if (placedHorses >= 3) {
    answer = mid;
    lt = mid + 1;
  } else rt = mid - 1;
}

console.log(answer);
