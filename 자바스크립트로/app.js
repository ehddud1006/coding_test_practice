n = 10;
function solution(n) {
  var answer = 0;
  let arr = new Array(n + 1).fill(true);

  for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
    if (!arr[i]) continue;

    for (let j = i * i; j <= n; j += i) {
      arr[j] = false;
    }
  }
  for (let i = 2; i <= n; i++) {
    if (arr[i]) answer += 1;
  }
  return answer;
}
solution(n);
