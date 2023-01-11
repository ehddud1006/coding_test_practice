const string = 'g0en2T0s8eSoft';
let selectNumberString = '';
for (const char of string) {
  if (!isNaN(char)) selectNumberString += char;
}

console.log(Number(selectNumberString));
