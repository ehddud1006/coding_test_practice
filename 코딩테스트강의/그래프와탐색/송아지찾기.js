const START = 8;
const END = 3;
const dx = [1, -1, 5];
const visited = Array.from({ length: 10001 }, () => false);
const queue = [];
queue.push([START, 0]);
visited[START] = true;

while (queue.length) {
  const [x, dist] = queue.shift();
  if (x === END) {
    console.log(dist);
    break;
  }

  for (let nd of dx) {
    const dx = x + nd;
    if (dx >= 1 && dx <= 10000 && !visited[dx]) {
      visited[dx] = true;
      queue.push([dx, dist + 1]);
    }
  }
}
