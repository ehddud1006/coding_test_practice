let a = [1, 3, 5];
let b = [2, 3, 6, 7, 9];
const solution = (a, b) => {
  let aLen = a.length;
  let bLen = b.length;
  let p1 = 0;
  let p2 = 0;
  let answer = [];
  while (p1 < aLen && p2 < bLen) {
    if (a[p1] <= b[p2]) answer.push(a[p1++]);
    // a[p1] 을 넣고 p1 포인터를 증가시킨다. (후위증가)
    else answer.push(b[p2++]);
  }
  while (p1 < aLen) answer.push(a[p1++]);
  while (p2 < bLen) answer.push(b[p2++]);

  return answer;
};

console.log(solution(a, b));
