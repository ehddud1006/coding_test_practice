const [start, end] = [8, 3];

const queue = [];
const action = [1, -1, 5];

queue.push([8, 0]);

while (queue.length) {
  let [location, count] = queue.shift();

  if (location === end) {
    console.log(count);
    break;
  }
  for (let i = 0; i < action.length; i++) {
    const nextLocation = location + action[i];
    if (nextLocation >= 1 && nextLocation <= 10_000) {
      queue.push([nextLocation, count + 1]);
    }
  }
}
