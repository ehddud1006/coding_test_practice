const arr = [
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

function DFS(x, y) {
  arr[x][y] = 0;
  for (let i = 0; i < 8; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (nx >= 0 && nx <= 6 && ny >= 0 && ny <= 6 && arr[nx][ny]) {
      DFS(nx, ny);
    }
  }
}

for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < arr[0].length; j++) {
    if (arr[i][j]) {
      count++;
      DFS(i, j);
    }
  }
}

console.log(count);
