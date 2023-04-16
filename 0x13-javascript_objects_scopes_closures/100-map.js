#!/usr/bin/node

const origList = require('./100-data').list;

const newList = origList.map((x, y) => x * y);
console.log(origList);
console.log(newList);
