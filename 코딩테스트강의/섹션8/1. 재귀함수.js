// const fs = require("fs");

// BOJkey = 1;

// let input = fs
//   .readFileSync(BOJkey ? "./자바스크립트로/10828/input.txt" : "./dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");

function solution(n) {
  function DFS(L) {
    if (L == 0) return;
    else {
      console.log(L);
      DFS(L - 1);
    }
  }
  DFS(n);
}

solution(3);
