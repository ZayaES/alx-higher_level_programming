#!/usr/bin/node

exports.logMe = function (item) {
  let argNum = 0;
  return function (item) {
    console.log(`${argNum}: ${item}`);
    argNum += 1;
    return argNum;
  }
}();
