#!/usr/bin/node
const list = require('./100-data').list;

// Compute a new array using map
const newList = list.map((value, index) => value * index);

// Print the initial list and the new list
console.log("Initial list:");
console.log(list);
console.log("New list:");
console.log(newList);
