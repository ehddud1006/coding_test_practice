let arr1 = [1, 3, 9, 5, 2];
let arr2 = [3, 2, 5, 7, 8];

arr1.sort();
arr2.sort();

let p1 = 0;
let p2 = 0;
let answer = [];
while (p1 < arr1.length && p2 < arr2.length) {
  if (arr1[p1] == arr2[p2]) {
    answer.push(arr1[p1++]);
    p2++;
  } else if (arr1[p1] < arr2[p2]) {
    p1++;
  } else p2++;
}

console.log(answer);

// -> 왜 sort를 하셨나요 라고 질문을 누가한다면..
// let arr1 = [1, 3, 9, 5, 2];
// let arr2 = [3, 2, 5, 7, 8];
// 1, 2, 3, 5, 9;
// 2, 3, 5, 7, 9;

// 투포인터를 사용하기위해 정렬을 했다.

// -> 그럼 왜 정렬을 해야 투포인터를 사용할 수 있나요?
// 이 문제 같은 경우에는 우선 두 배열의 요소 중 같은 값을 찾아내는 것입니다.
// 정렬해놓아야 포인터를 증가시켰을때 그 다음값이 현재값보다 더 큰 값이라는 것을 보장할 수 있습니다.
// 그렇기때문에 포인터를 증가시키는 과정을 통해 같은 값을 찾을 수 있습니다.
