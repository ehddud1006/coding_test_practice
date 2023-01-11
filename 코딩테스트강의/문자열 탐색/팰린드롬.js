let string = 'found7, time: study; Yduts; emit, 7Dnuof';

const check_eng = /[a-z]/; // 문자
string = string.toLowerCase();
string = string
  .split('')
  .map(char => {
    if (check_eng.test(char)) return char;
  })
  .join('');

reverseString = string.split('').reverse().join('');
if (string === reverseString) console.log('YES');
else console.log('NO');

// function solution(s){
//     let answer="YES";
//     s=s.toLowerCase().replace(/[^a-z]/g, '');
//     if(s.split('').reverse().join('')!==s) return "NO";
//     return answer;
// }

// let str="found7, time: study; Yduts; emit, 7Dnuof";
// console.log(solution(str));
