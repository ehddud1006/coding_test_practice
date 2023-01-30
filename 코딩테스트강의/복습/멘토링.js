const N = 4;
const M = 3;
const test = [
  [3, 4, 1, 2],
  [4, 3, 2, 1],
  [3, 1, 4, 2],
];

const matchStudentList = [];
const visited = Array.from({ length: N + 1 }, () => false);
const tmp = [];

const matchStudent = L => {
  if (L === 2) {
    matchStudentList.push([...tmp]);
    return;
  }
  for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
      tmp.push(i);
      visited[i] = true;
      matchStudent(L + 1);
      visited[i] = false;
      tmp.pop();
    }
  }
};

matchStudent(0);
let count = 0;

for (let [mentor, mentee] of matchStudentList) {
  flag = true;
  for (let i = 0; i < M; i++) {
    let [mentorIndex, menteeIndex] = [0, 0];
    for (let j = 0; j < N; j++) {
      if (test[i][j] === mentor) mentorIndex = j;
      if (test[i][j] === mentee) menteeIndex = j;
    }
    if (mentorIndex > menteeIndex) {
      flag = false;
      break;
    }
  }

  if (flag) count++;
}

console.log(count);
