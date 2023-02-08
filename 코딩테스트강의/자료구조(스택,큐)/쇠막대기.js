const str = '(((()(()()))(())()))(()())';
const stack = [];
let count = 0;
let prev = '';

for (let x of str) {
  console.log(`stack: ${stack} count:${count}`);
  if (x === '(') {
    stack.push(x);
    prev = x;
  }
  if (x === ')') {
    stack.pop();
    if (prev === x) {
      count++;
    } else {
      count += stack.length;
    }
    prev = x;
  }
}

console.log(count);
