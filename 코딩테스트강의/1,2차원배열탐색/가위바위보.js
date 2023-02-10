const N = 10;
const arr = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0];
let number = 0;
let sum = 0;

arr.forEach(element => {
  if (element === 1) number++;
  else number = 0;

  sum += number;
});

console.log(sum);
