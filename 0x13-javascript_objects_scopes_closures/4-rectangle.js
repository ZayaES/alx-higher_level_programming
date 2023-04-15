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

  rotate () {
    const c = this.width;
    this.width = this.height;
    this.height = c;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
