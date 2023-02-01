let string = 'Lava';

string = string.toLocaleLowerCase();

const lastIndex = string.length - 1;
flag = true;

for (let i = 0; i < parseInt(string.length / 2); i++) {
  if (string[i] !== string[lastIndex - i]) flag = false;
}

if (flag) console.log('YES');
else console.log('NO');
