function solution(answers) {
  var answer = [];
  let arr1 = [1, 2, 3, 4, 5];
  let arr2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let count = new Array(3);
  count.fill(0);
  answers.map((el, idx) => {
    // console.log(el,arr1[idx%5],arr2[idx%8],arr3[idx%10])
    if (arr1[idx % 5] == el) {
      count[0]++;
    }
    if (arr2[idx % 8] == el) {
      count[1]++;
    }
    if (arr3[idx % 10] == el) {
      count[2]++;
    }
  });
  count_max = Math.max(...count);
  console.log(count_max);
  count.map((el, idx) => {
    if (count_max == el) {
      answer.push(idx + 1);
    }
  });
  return answer;
}
