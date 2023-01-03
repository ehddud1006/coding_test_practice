const input1 = 'abaCC';
const input2 = 'Caaab';

const input1Array = input1.split('');
const input2Array = input2.split('');

const input1Map = new Map();
const input2Map = new Map();

input1Array.forEach(alphabet => {
  input1Map.set(alphabet, input1Map.get(alphabet) + 1 || 1);
});

input2Array.forEach(alphabet => {
  input2Map.set(alphabet, input2Map.get(alphabet) + 1 || 1);
});

let flag = true;
for (let item of input1Map) {
  if (input1Map.get(item[0]) !== input2Map.get(item[0])) flag = false;
}

console.log(flag ? 'YES' : 'NO');
