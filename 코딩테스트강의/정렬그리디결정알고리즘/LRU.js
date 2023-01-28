const S = 5;
const N = 9;
const arr = [1, 2, 3, 2, 6, 2, 3, 5, 7];

const cache = Array.from({ length: 5 }, () => 0);

for (let i = 0; i < N; i++) {
  let index = cache.indexOf(arr[i]);
  let tmp = 0;
  let j = 0;
  if (index === -1) {
    tmp = arr[i];
    index = S - 1;
  } else {
    tmp = arr[index];
  }
  for (j = index - 1; j >= 0; j--) {
    cache[j + 1] = cache[j];
  }
  cache[j + 1] = tmp;
}

console.log(cache);
