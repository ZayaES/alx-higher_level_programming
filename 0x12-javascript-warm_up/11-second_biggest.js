#!/usr/bin/node

const array = [];
const len = process.argv.length;
if (len < 4) {
  console.log('0');
} else {
  for (let i = 2; i < len; i++) {
    arg = parseInt(process.argv[i]);
    array[i - 2] = arg;
  }
  array.sort();
  array.reverse();
  console.log(array[1]);
}
