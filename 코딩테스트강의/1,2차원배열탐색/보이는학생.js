const N = 8;
const students = [130, 135, 148, 140, 145, 150, 150, 153];

let currentBiggestStudent = Number.MIN_SAFE_INTEGER;

let count = 0;

students.forEach(student => {
  if (student > currentBiggestStudent) {
    currentBiggestStudent = student;
    count++;
  }
});

console.log(count);
