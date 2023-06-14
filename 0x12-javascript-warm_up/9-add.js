#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const add1 = parseInt(process.argv[2]);
const add2 = parseInt(process.argv[3]);
console.log(add(add1, add2));
