numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
hand = "right";
const keys = {
  1: [0, 0],
  2: [0, 1],
  3: [0, 2],
  4: [1, 0],
  5: [1, 1],
  6: [1, 2],
  7: [2, 0],
  8: [2, 1],
  9: [2, 2],
  "*": [3, 0],
  0: [3, 1],
  "#": [3, 2],
};

const getDistance = (arr1, arr2) => {
  const [x1, y1] = arr1;
  const [x2, y2] = arr2;
  return Math.abs(x1 - x2) + Math.abs(y1 - y2);
};
function solution(numbers, hand) {
  let answer = [];
  let leftHand = keys["*"];
  let rightHand = keys["#"];
  numbers.map((el, index) => {
    let l = getDistance(keys[el], leftHand);
    let r = getDistance(keys[el], rightHand);
    if (el == 1 || el == 4 || el == 7) {
      leftHand = keys[el];
      answer.push("L");
    } else if (el == 3 || el == 6 || el == 9) {
      rightHand = keys[el];
      answer.push("R");
    } else {
      let l = getDistance(keys[el], leftHand);
      let r = getDistance(keys[el], rightHand);
      if (l < r) {
        leftHand = keys[el];
        answer.push("L");
      } else if (r < l) {
        rightHand = keys[el];
        answer.push("R");
      } else {
        if (hand == "right") {
          rightHand = keys[el];
          answer.push("R");
        } else {
          leftHand = keys[el];
          answer.push("L");
        }
      }
    }
  });
  //   console.log(answer);
  ans = answer.join("");
  //   console.log(ans);
  return ans;
}

solution(numbers, hand);
