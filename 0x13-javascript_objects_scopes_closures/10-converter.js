#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (base === 10) {
      return number;
    } else {
      let result = '';
      const letDigit = ['a', 'b', 'c', 'd', 'e', 'f'];
      while (number !== 0) {
        let rem = number % base;
        if (rem >= 10) {
          rem = letDigit[rem % 10];
        }
        result += rem;
        number = Math.floor(number / base);
      }
      return [...result].reverse().join('');
    }
  };
};
