str = '(()(()))(()';
stack = [];
answer = 'YES';
for (let x of str) {
  if (x === '(') stack.push(x);
  if (x === ')') {
    if (stack.length) {
      stack.pop();
    } else {
      break;
    }
  }
}

if (stack.length > 0) answer = 'NO';
console.log(answer);
