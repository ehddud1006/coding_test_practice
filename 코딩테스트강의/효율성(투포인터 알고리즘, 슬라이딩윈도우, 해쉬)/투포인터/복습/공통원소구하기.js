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
