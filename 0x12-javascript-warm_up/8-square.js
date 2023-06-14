#!/usr/bin/node

const arg = parseInt(process.argv[2]);
if (arg) {
  let sym = '';
  for (let i = 0; i < arg; i++) {
    sym = sym + 'X';
  }
  for (let i = 0; i < arg; i++) {
    console.log(sym);
  }
} else {
  console.log('Missing size');
}
