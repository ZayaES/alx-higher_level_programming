#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const size = list.length;

  for (let i = 0; i < size; i++) {
    newList[i] = list[size - 1 - i];
  }
  return newList;
};
