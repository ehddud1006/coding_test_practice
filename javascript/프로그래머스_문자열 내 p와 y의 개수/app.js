s = "pPoooyY";
function solution(s) {
  var answer = true;
  let yCount = 0;
  let pCount = 0;

  s.toLowerCase();
  let arr = s.split("");
  arr.map((el) => {
    if (el == "y") yCount++;
    else pCount++;
  });
  if (yCount != pCount) answer = false;
  if (yCount == 0 && pCount == 0) answer = true;
  return answer;
}

solution(s);
