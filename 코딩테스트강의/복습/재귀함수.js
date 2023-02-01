const N = 12;

let binary = '';
const dfs = n => {
  if (n === 1) {
    binary += '1';
    return;
  }
  dfs(parseInt(n / 2));
  binary += String(n % 2);
};

dfs(N);

console.log(binary);
