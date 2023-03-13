#!/usr/bin/node

function factorial (num) {
  if (!parseInt(num)) { return (1); }

  parseInt(num);
  if (num === 1) { return (1); }

  return (num * factorial(num - 1));
}

console.log(factorial(process.argv[2]));
