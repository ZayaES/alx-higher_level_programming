#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (base === 10) {
      return number;
    } else {
      return (number.toString(base));
    }
  };
};
