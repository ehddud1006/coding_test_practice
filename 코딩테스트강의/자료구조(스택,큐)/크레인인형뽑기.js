const board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];
const moves = [1, 5, 3, 5, 1, 2, 1, 4];
const stack = [];
let count = 0;

moves.forEach(move => {
  let doll = 0;
  for (let i = 0; i < board.length; i++) {
    let checkArea = board[i][move - 1];
    if (checkArea > 0) {
      doll = checkArea;
      board[i][move - 1] = 0;
      break;
    }
  }

  if (doll > 0 && stack.at(-1) === doll) {
    count += 2;
    stack.pop();
  } else stack.push(doll);
});

console.log(count);
