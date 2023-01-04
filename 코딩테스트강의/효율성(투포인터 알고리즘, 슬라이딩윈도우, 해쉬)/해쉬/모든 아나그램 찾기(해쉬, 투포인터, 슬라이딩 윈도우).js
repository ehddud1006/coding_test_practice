const S = 'bacaAacba';
const T = 'abc';

// 뭐부터해야하지
// 우선 T의 Map을 구해야해

const Tmap = new Map();
const Smap = new Map();
let answer = 0;
for (const alphabet of T) {
  Tmap.set(alphabet, Tmap.get(alphabet) + 1 || 1);
}

console.log(Tmap);

// 집중좀해라
// 이제 뭐해야되는데  슬라이딩 윈도우 만들어야지

let lp = 0;
let rp = T.length - 1;

for (let i = 0; i < T.length; i++) {
  Smap.set(S[i], Smap.get(S[i]) + 1 || 1);
}

const isAnagram = () => {
  for (let item of Tmap) {
    if (item[1] !== Smap.get(item[0])) return false;
  }
  return true;
};
while (rp <= S.length) {
  console.log(Smap);
  if (isAnagram()) answer++;
  Smap.set(S[++rp], Smap.get(S[rp]) + 1 || 1);
  Smap.set(S[lp], Smap.get(S[lp++]) - 1);
}

console.log(answer);
