const N = 4;
const M = 5;
let arr = [1, 2, 2, 3];
let lp = 0;
let rp = 0;
let sum = 0;
let plusFlag = true;
let count = 0;
while (rp < N) {
  if (plusFlag) sum += arr[rp];
  if (sum <= M) {
    // for (let copyRp = rp; copyRp >= lp; copyRp--) {
    //   count++;
    // }
    count += rp - lp + 1;
    rp++;
    plusFlag = true;
  } else {
    sum -= arr[lp++];
    plusFlag = false;
  }
}

console.log(count);
