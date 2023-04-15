#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let result = '';
    for (let i = 0; i < this.width; i++) {
      result += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(result);
    }
  }
}
module.exports = Rectangle;
