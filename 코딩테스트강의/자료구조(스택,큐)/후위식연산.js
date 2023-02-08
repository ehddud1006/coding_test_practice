const str = '352+*9-';
const stack = [];

for (let x of str) {
  let [a, b] = [0, 0];
  console.log(stack);
  switch (x) {
    case '+':
      a = stack.pop();
      b = stack.pop();
      stack.push(b + a);
      break;
    case '-':
      a = stack.pop();
      b = stack.pop();
      stack.push(b - a);
      break;
    case '/':
      a = stack.pop();
      b = stack.pop();
      stack.push(b / a);
      break;
    case '*':
      a = stack.pop();
      b = stack.pop();
      stack.push(b * a);
      break;
    default:
      stack.push(parseInt(x));
  }
}

console.log(stack.pop());
