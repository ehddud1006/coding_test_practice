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
let count = 0;

function dfs(x, y) {
  for (let i = 0; i < dx.length; i++) {
    const [nx, ny] = [x + dx[i], y + dy[i]];
    if (nx >= 0 && nx <= 6 && ny >= 0 && ny <= 6 && graph[nx][ny] === 1) {
      graph[nx][ny] = 0;
      dfs(nx, ny);
    }
  }
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (graph[i][j] === 1) {
      count++;
      graph[i][j] = 0;
      dfs(i, j);
    }
  }
}

console.log(count);
