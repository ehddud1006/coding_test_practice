let input = [
  [1, 3],
  [2, 6],
  [6, 10],
  [8, 18],
];

let ans = [];
let queue = [];
queue.push(input.shift());
queue.push(input.shift());

while (input.length >= 0) {
  if (queue[0][1] >= queue[1][0]) {
    let temp = [queue[0][0], queue[1][1]];
    queue.pop();
    queue.pop();
    queue.push(temp);
  }
  if (input.length === 0) {
    break;
  } else {
    queue.push(input.shift());
  }
}

console.log(queue);
