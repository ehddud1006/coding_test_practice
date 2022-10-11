let board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];

let moves = [1, 5, 3, 5, 1, 2, 1, 4];
function solution(board, moves) {
  var answer = 0;
  let stack = [];
  let len = board.length;
  moves.map((el) => {
    for (let i = 0; i < len; i++) {
      console.log(board[i][el - 1]);
      if (board[i][el - 1] != 0) {
        if (stack.length > 0 && stack[stack.length - 1] == board[i][el - 1]) {
          stack.pop();
          board[i][el - 1] = 0;
          answer += 2;
        } else {
          stack.push(board[i][el - 1]);
          board[i][el - 1] = 0;
        }
        break;
      }
    }
  });

  return answer;
}

solution(board, moves);
