const arr1 = [1, 3, 9, 5, 2];
const arr2 = [3, 2, 5, 7, 8];
let upperP = 0;
let lowerP = 0;
const answer = [];

arr1.sort();
arr2.sort();

while (upperP < arr1.length && lowerP < arr2.length) {
  if (arr1[upperP] < arr2[lowerP]) upperP++;
  else if (arr1[upperP] === arr2[lowerP]) {
    answer.push(arr1[upperP++]);
    lowerP++;
  } else lowerP++;
}

console.log(answer);

// 씨.. 또 못풀었다. 실버 5인데 나는 병신인가보다.
// 1 3 5
// 2 3 6 7 9 일때 투 포인터로 접근해야하는 것은 당연히 문제 카테고리가 투포인터라서 알고 있었다.
// 근데 while 문의 범위를 어떻게 정해야할지 모르겠더라. 이걸 왜 생각을 못하니..
// 투포인터로 접근했을때 분명히 하나의 배열을 먼저 다 순회할 것이다. 그때의 case 를 나누어야했네 보니까.

// if(arr1.length >= arr2.length){
// 	while (upperP < arr1.length){
// 		if (arr1[upperP] >= arr2[lowerP]) answer.push(arr2[lowerP++]);
// 	    else answer.push(arr1[upperP++]);
// 	}
// 	while (upperP < arr1.length) answer.push(arr1[upperP++]);

// }
// else{
//  while(lowerP < arr2.length) {
// 		if (arr1[upperP] >= arr2[lowerP]) answer.push(arr2[lowerP++]);
// 		else answer.push(arr1[upperP++]);
//   }
//   while (lowerP < arr2.length) answer.push(arr2[lowerP++]);
// }

// 해설해서는 if else 로 분기처리 하지 않고 &&  연산자를 사용하여 우아하게 분기처리를 했다.
// while (upperP < arr1.length && lowerP < arr2.length)

// ******************************************************
// 23.01.29
// 또 못풀었다. 이번에는 정렬을 하지 않고 풀어버렸는데, 작은값의 포인터를 증가시키는 방식에서
// [1,3,9,5,2]
// [3,2,5,7,8]
// lt가 9에서 멈춰버렸다. 따라서 rt 는 계속 증가하여 배열순회가 끝나버리니 [3]밖에 찾을 수가 없었다.
// 따라서 위와 같은 로직을 사용하기 위해서는 정렬이라는 전제조건이 필요하다.

// const arr1 = [1, 3, 9, 5, 2];
// const arr2 = [3, 2, 5, 7, 8];

// let [lt, rt] = [0, 0];

// const answer = [];

// arr1.sort();
// arr2.sort();

// while (lt !== arr1.length && rt !== arr2.length) {
//   console.log(arr1[lt]);
//   if (arr1[lt] < arr2[rt]) lt++;
//   else if (arr1[lt] > arr2[rt]) rt++;
//   else {
//     answer.push(arr1[lt++]);
//     rt++;
//   }
// }

// console.log(answer);
