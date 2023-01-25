const N = 8;
const arr = [5, 3, 7, 8, 6, 2, 9, 4];
const dy = Array.from({ length: N + 1 }, () => 0);
let answer = Number.MIN_SAFE_INTEGER;
for (let i = 0; i < N; i++) {
  let max = 0;
  for (let j = i; j >= 0; j--) {
    if (arr[j] < arr[i] && max < dy[j]) {
      max = dy[j];
    }
  }
  dy[i] = max + 1;
  answer = Math.max(answer, max + 1);
}

console.log(answer);
