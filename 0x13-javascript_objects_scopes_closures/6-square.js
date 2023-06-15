#!/usr/bin/node

const Squares = require('./5-square');

module.exports = class Square extends Squares {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let sym = '';
      for (let i = 0; i < this.width; i++) {
        sym = sym + c;
      }
      for (let i = 0; i < this.width; i++) {
        console.log(sym);
      }
    }
  }
};
