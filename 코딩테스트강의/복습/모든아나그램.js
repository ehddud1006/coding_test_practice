const S = 'bacaAacba';
const T = 'abc';

const Smap = new Map();
const Tmap = new Map();
const searchLength = T.length;

let [lt, rt] = [0, searchLength - 1];
let count = 0;

for (let i = 0; i < searchLength; i++) {
  Tmap.set(T[i], Tmap.get(T[i]) + 1 || 1);
}

const TmapToArray = [...Tmap];

for (let i = lt; i <= rt; i++) {
  Smap.set(S[i], Smap.get(S[i]) + 1 || 1);
}

while (rt < S.length) {
  flag = true;
  for (let [key, value] of TmapToArray) {
    if (Smap.get(key) !== value) flag = false;
  }
  if (flag) count++;
  Smap.set(S[++rt], Smap.get(S[rt]) + 1 || 1);
  Smap.set(S[lt], Smap.get(S[lt++]) - 1);
}

console.log(count);
