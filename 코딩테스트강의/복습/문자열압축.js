const string = 'KKHSSSSSSSE';

let target = string[0];
let count = 0;
let newString = '';
for (let i = 0; i < string.length; i++) {
  if (target !== string[i]) {
    newString += target + count.toString();
    target = string[i];
    count = 1;
  } else count++;
}

newString += target + count.toString();

newString = newString.split('').reduce((str, curr) => {
  if (curr === '1') return str;
  return (str += curr);
}, '');

console.log(newString);
