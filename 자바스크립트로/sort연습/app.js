var employees = [
  { name: "홍길동", salary: 30000 },
  { name: "김길동", salary: 10000 },
  { name: "마이콜", salary: 20000 },
];

employees.sort(function compare(a, b) {
  return b.salary - a.salary;
});

console.log(employees);
/* result
 [d
  { name: '홍길동', salary: 30000 },
  { name: '마이콜', salary: 20000 },
  { name: '김길동', salary: 10000 },
]
  */
