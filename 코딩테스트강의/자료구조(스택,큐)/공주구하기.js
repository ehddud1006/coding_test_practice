const [N, K] = [8, 3];

const queue = [];

for (let i = 1; i <= N; i++) {
  queue.push(i);
}

queue = Array.from({ length: N }, (v, i) => i + 1);

let count = 1;
while (queue.length !== 1) {
  console.log(`queue: ${queue} count: ${count}`);
  if (count === 3) {
    queue.shift();
    count = 1;
  } else {
    queue.push(queue.shift());
    count++;
  }
}

console.log(queue.pop());
