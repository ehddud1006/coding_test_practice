new_id = "...!@BaT#*..y.abcdefghijklm";
function solution(new_id) {
  var answer = "";
  console.log(new_id);
  new_id = new_id.toLowerCase();
  console.log(new_id);
  new_id = new_id.replace(/[!@$*]/g, "");
  console.log(new_id);
  return answer;
}

solution(new_id);
