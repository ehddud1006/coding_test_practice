nums = [1, 2, 3, 4];

function combination(arr, selectNum) {
  let result = [];
  if (selectNum == 1) return arr.map((v) => [v]);
  arr.map((v, index, arr) => {
    const fixed = v;
    const restArr = arr.slice(index + 1);
    const combinationArr = combination(restArr, selectNum - 1);
    const combineFix = combinationArr.map((v) => [fixed, ...v]);
    result.push(...combineFix);
  });
  return result;
}

function solution(nums) {
  count = 0;
  let key = combination(nums, 3);
  for (let [a, b, c] of key) {
    let sum = a + b + c;
    let check = true;
    for (let i = 2; i < sum; i++) {
      if (sum % i == 0) {
        check = false;
        break;
      }
    }
    if (check) count++;
  }
  console.log(count);
  return count;
}

solution(nums);
