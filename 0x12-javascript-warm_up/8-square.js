#!/usr/bin/node

const squSize = parseInt(process.argv[2]);
let result = '';
if (Number.isNaN(squSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squSize; i++) {
    result += 'X';
  }
  for (let j = 0; j < squSize; j++) {
    console.log(result);
  }
}
