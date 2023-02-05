const graph = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 1, 0, 0, 0],
  [1, 1, 0, 1, 0, 1, 1],
  [1, 1, 0, 0, 0, 0, 1],
  [1, 1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 0, 0],
];

let count = 0;
const dx = [0, 1, 0, -1];
const dy = [-1, 0, 1, 0];

function dfs(x, y) {
  if (x === 6 && y === 6) {
    count++;
    return;
  }
  for (let i = 0; i < 4; i++) {
    const [nx, ny] = [x + dx[i], y + dy[i]];
    if (nx >= 0 && nx <= 6 && ny >= 0 && ny <= 6 && graph[nx][ny] === 0) {
      graph[nx][ny] = 1;
      dfs(nx, ny);
      graph[nx][ny] = 0;
    }
  }
}

graph[0][0] = 1;
dfs(0, 0);

console.log(count);
