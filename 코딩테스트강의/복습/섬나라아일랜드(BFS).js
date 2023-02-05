const N = 7;

const graph = [
  [1, 1, 0, 0, 0, 1, 0],
  [0, 1, 1, 0, 1, 1, 0],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 1, 1],
  [1, 1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 1, 0, 0],
  [1, 0, 1, 0, 1, 0, 0],
];

const dx = [0, 1, 1, 1, 0, -1, -1, -1];
const dy = [-1, -1, 0, 1, 1, 1, 0, -1];
const queue = [];

let count = 0;

for (let i = 0; i < graph.length; i++) {
  for (let j = 0; j < graph[0].length; j++) {
    if (graph[i][j] === 1) {
      count++;
      queue.push([i, j]);

      while (queue.length) {
        let [x, y] = queue.shift();

        for (let i = 0; i < dx.length; i++) {
          const [nx, ny] = [x + dx[i], y + dy[i]];
          if (nx >= 0 && nx <= 6 && ny >= 0 && ny <= 6 && graph[nx][ny] === 1) {
            graph[nx][ny] = 0;
            queue.push([nx, ny]);
          }
        }
      }
    }
  }
}

console.log(count);
