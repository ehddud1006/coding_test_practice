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
const queue = [];

let count = 0;

for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < arr[0].length; j++) {
    if (arr[i][j]) {
      count++;
      queue.push([i, j]);
      arr[i][j] = 0;
      while (queue.length) {
        const [x, y] = queue.shift();
        for (let k = 0; k < 8; k++) {
          const nx = x + dx[k];
          const ny = y + dy[k];
          if (nx >= 0 && nx <= 6 && ny >= 0 && ny <= 6 && arr[nx][ny]) {
            arr[nx][ny] = 0;
            queue.push([nx, ny]);
          }
        }
      }
    }
  }
}

console.log(count);
