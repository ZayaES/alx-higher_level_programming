#!/usr/bin/node

const Squares = require('./5-square');

module.exports = class Square extends Squares {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    if (!c) {
      this.print();
    } else {
      let sym = c;
      for (let i = 0; i < this.width; i++) {
        sym = sym + c;
      }
      for (let i = 0; i < this.width; i++) {
        console.log(sym);
      }
      }
  }
}
