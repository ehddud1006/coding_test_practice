const combination = (arr, selectNum) => {
  const result = [];
  if (selectNum === 1) return arr.map((v) => [v]);
  arr.map((v, index, arr) => {
    const fixed = v;
    const restArr = arr.slice(index + 1);
    const combinationArr = combination(restArr, selectNum - 1);
    const combineFix = combinationArr.map((v) => [fixed, ...v]);
    result.push(...combineFix);
  });
  return result;
};

const a = combination([1, 2, 3, 4], 2);

console.log(a);
