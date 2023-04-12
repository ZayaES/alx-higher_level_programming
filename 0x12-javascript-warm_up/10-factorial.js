#!/usr/bin/node

function factorial (a) {
  if (Number.isNaN(a) || (a === 0) || (a === 1)) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

const ans = factorial(parseInt(process.argv[2]));
console.log(ans);
