const string = 'goog';

const str = string.toLowerCase();
const stack = [];
const len = str.length;
for (let i = 0; i < len / 2; i++) {
  stack.push(str[i]);
}

if (len % 2 === 1) {
  for (let i = len / 2 + 1; i < len; i++) {
    if (stack[stack.length - 1] === str[i]) stack.pop();
  }
} else {
  for (let i = len / 2; i < len; i++) {
    if (stack[stack.length - 1] === str[i]) {
      stack.pop();
    }
  }
}

if (stack.length === 0) console.log('YES');
else console.log('NO');

// function solution(s){
//     let answer="YES";
//     s=s.toLowerCase();
//     let len=s.length;
//     for(let i=0; i<Math.floor(len/2); i++){
//         if(s[i]!=s[len-i-1]) return "NO";
//     }
//     return answer;
// }
