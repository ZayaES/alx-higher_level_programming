#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let count = 0;

  console.log(list);
  while (list[i] !== searchElement) {
    i++;
    if (i === list.length) {
      return 0;
    }
  }
  while (list[i] === searchElement) {
    count = count + 1;
    i++;
  }
  return count;
};
