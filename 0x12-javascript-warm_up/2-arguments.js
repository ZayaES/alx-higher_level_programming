#!/usr/bin/node

function argMes () {
  let i = 0;
  while (process.argv[i + 2] != null) {
    i = i + 1;
  }
  if (i === 0) {
    console.log('No argument');
  } else if (i === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

argMes();
