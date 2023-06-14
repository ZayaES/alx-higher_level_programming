#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function factorial (num) {
  if (!num) {
    return (1);
  }
  if ((num === 0) || (num === 1)) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

console.log(factorial(arg));
