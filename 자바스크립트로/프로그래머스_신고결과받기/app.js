let id_list = ["muzi", "frodo", "apeach", "neo"];
let report = [
  "muzi frodo",
  "apeach frodo",
  "frodo neo",
  "muzi neo",
  "apeach muzi",
];
let k = 2;
function solution(id_list, report, k) {
  const arr = ["A", "B", "C", "A", "B"];

  const initialValue = [];
  const newArr = arr.reduce(
    (acc, obj) => (acc.includes(obj) ? acc : [...acc, obj]),
    initialValue
  );
  console.log(newArr);

  let answer = [];
  console.log(report[-1]);
  // 중복 제거 후, 유저 ID, 유저가 신고한 ID 분리
  let reports = [...new Set(report)].map((el) => el.split(" "));

  // 신고 당한 ID Map
  let reportId = new Map();

  // 신고 당한 ID 카운트
  for ([, report] of reports) {
    reportId.set(report, reportId.get(report) + 1 || 1);
  }

  // 메일 발송 ID Map
  let mailId = new Map();

  // 메일 발송 갯수 카운트
  for ([user, report] of reports) {
    if (reportId.get(report) >= k) {
      mailId.set(user, mailId.get(user) + 1 || 1);
    }
  }

  // 메일 발송 추출 (없는 경우 0)
  answer = id_list.map((id) => mailId.get(id) || 0);

  return answer;
}

console.log(solution(id_list, report, 2));

const id_list2 = ["con", "ryan"];
const report2 = ["ryan con", "ryan con", "ryan con", "ryan con"];
console.log(solution(id_list2, report2, 3));

solution(id_list, report, k);
