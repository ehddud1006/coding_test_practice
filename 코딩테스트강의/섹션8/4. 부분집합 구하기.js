input = 3;
check = new Array(input + 1).fill(false);
result = "";
const dfs = (v) => {
  if (v === input + 1) {
    result = "";
    for (let i = 1; i <= input; i++) {
      if (check[i]) result += `${i} `;
    }
    console.log(result);
  } else {
    check[v] = true;
    dfs(v + 1);
    check[v] = false;
    dfs(v + 1);
  }
};

dfs(1);
