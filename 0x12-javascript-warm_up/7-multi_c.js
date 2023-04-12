#!/usr/bin/node

const occNum = parseInt(process.argv[2]);
if (Number.isNaN(occNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occNum; i++) {
    console.log('C is fun');
  }
}
