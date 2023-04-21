#!/usr/bin/node

const Square = require('./5-square');

class Square extends Square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let result = '';
      for (let i = 0; i < this.width; i++) {
        result += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(result);
      }
    }
  }
}

module.exports = Square;