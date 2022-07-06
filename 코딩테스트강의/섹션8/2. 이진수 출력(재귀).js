function solution(n) {
  let answer = "";
  const dfs = (n) => {
    if (n === 0) {
      return;
    } else {
      dfs(parseInt(n / 2));
      console.log(n % 2);
    }
  };
  dfs(n);
  return answer;
}

solution(11);
