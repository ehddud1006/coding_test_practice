queue = [];
queue.push(1);

while (queue.length) {
  let v = queue.shift();
  console.log(v);
  for (let x of [2 * v, 2 * v + 1]) {
    if (x <= 7) queue.push(x);
  }
}
