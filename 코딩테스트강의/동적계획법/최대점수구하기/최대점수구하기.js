const fs = require('fs');

BOJkey = 1;

const readInput = fs
  .readFileSync(BOJkey ? './코딩테스트강의/동적계획법/최대점수구하기/input.txt' : './dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, M] = readInput.shift().split(' ').map(Number);

const input = readInput.map(el => el.split(' ').map(Number));
const dp = Array.from({ length: M + 1 }, () => 0);

for (let [score, time] of input) {
  for (let i = M; i >= time; i--) {
    dp[i] = Math.max(dp[i], dp[i - time] + score);
  }
}

console.log(dp);
