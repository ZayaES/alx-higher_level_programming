#!/usr/bin/node

origList = require('./100-data').list

newList = origList.map(x => x * origList.indexOf(x));
console.log(origList);
console.log(newList);
