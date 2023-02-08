let order = 'CBA';
let subject = 'CBDAGE';
subject = subject.split('');
console.log(subject);
let str = subject.reduce((str, element) => {
  if (order.includes(element)) return (str += element);
  return str;
}, '');

if (str === order) console.log('YES');
else console.log('NO');
