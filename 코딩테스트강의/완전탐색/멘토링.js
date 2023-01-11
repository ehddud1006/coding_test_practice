const N = 4;
const M = 3;
const test = [
  [3, 4, 1, 2],
  [4, 3, 2, 1],
  [3, 1, 4, 2],
];

let answer = 0;

for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= N; j++) {
    let count = 0;
    for (let s = 0; s < M; s++) {
      let pi = 0;
      let pj = 0;
      for (let k = 0; k < N; k++) {
        if (test[s][k] === i) pi = k;
        if (test[s][k] === j) pj = k;
      }
      if (pi < pj) count++;
    }
    if (count === M) answer++;
  }
}

console.log(answer);
