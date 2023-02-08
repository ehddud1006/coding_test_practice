const str = '(A(BC)D)EF(G(H)(IJ)K)LM(N)';
const stack = [];

for (let x of str) {
  if (x === ')') {
    while (stack.pop() !== '(');
    // while (true) {
    //   if (stack[stack.length - 1] === '(') {
    //     stack.pop();
    //     break;
    //   } else stack.pop();
    // }
  } else stack.push(x);
}

console.log(stack.join(''));
