#!/usr/bin/node
const nbOccurences = require('./7-occurences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));
console.log(nbOccurences([2, 4, 9, 22], 22));
