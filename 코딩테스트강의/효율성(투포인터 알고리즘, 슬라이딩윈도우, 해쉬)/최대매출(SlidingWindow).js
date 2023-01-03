let N = 10;
let K = 3;
let arr = [12, 15, 11, 20, 25, 10, 20, 19, 13, 15];

let answer = 0;
for (let i = 0; i < K; i++) {
  answer += arr[i];
}
let localSum = answer;

for (let i = K; i < N; i++) {
  localSum = localSum + arr[i] - arr[i - 3];
  //   if (answer < localSum) {
  //     answer = localSum;
  //   }
  // 위 if 문을 아래의 max 를 사용하여 한줄로 바꿀 수 있다.
  answer = Math.max(answer, sum);
}

console.log(answer);
