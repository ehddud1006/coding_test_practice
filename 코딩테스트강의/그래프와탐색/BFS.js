let answer = '';
let queue = [];

queue.push(1);

while (queue.length) {
  let v = queue.shift();
  answer += v + ' ';
  for (let nv of [2 * v, 2 * v + 1]) {
    if (nv <= 7) {
      queue.push(nv);
    }
  }
}

console.log(answer);
