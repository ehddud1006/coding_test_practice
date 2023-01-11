const string = 'KKHSSSSSSSE';

let cnt = 1;
let answer = '';
string.split('').forEach((char, index, arr) => {
  if (arr[index] === arr[index + 1]) {
    cnt++;
  } else if (arr[index] !== arr[index + 1] && cnt !== 1) {
    answer += char + cnt;
    cnt = 1;
  } else {
    answer += char;
  }
});

console.log(answer);
