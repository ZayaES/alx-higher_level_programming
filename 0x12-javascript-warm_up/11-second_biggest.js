#!/usr/bin/node

if (Number.isNaN(parseInt(process.argv[2])) || Number.isNaN(parseInt(process.argv[3]))) {
  console.log('0');
} else {
  let i = 2;
  let biggest = process.argv[i];
  let sndBiggest = process.argv[i + i];
  while (process.argv[i + 1]) {
    if (biggest > process.argv[i + 1]) {
      if (sndBiggest > process.argv[i + 1]);
      else {
        sndBiggest = process.argv[i + 1];
      }
    } else {
      sndBiggest = biggest;
      biggest = process.argv[i + 1];
    }
    i++;
  }
  console.log(sndBiggest);
}
