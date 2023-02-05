const S = 5;
const N = 9;
const arr = [1, 2, 3, 2, 6, 2, 3, 5, 7];

const cache = Array.from({ length: 5 }, () => 0);

for (let i = 0; i < arr.length; i++) {
  const process = arr[i];

  const index = cache.indexOf(process);
  if (index === -1) {
    cache.unshift(process);
    cache.pop();
  } else {
    for (let j = index - 1; j >= 0; j--) {
      cache[j + 1] = cache[j];
    }
    cache[0] = process;
  }
}

console.log(cache);
