participant = ["leo", "kiki", "eden"];
completion = ["eden", "kiki"];
function solution(participant, completion) {
  var answer = "";
  let report = new Map();
  participant.map((el) => {
    report.set(el, report.get(el) + 1 || 1);
  });
  completion.map((el) => {
    report.set(el, report.get(el) - 1 || 0);
  });
  for (const [key, value] of report) {
    if (value > 0) {
      answer = key;
    }
  }
  return answer;
}

solution(participant, completion);
