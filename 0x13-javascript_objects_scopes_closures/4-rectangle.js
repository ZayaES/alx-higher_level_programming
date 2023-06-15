#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let sym = '';
    for (let i = 0; i < this.width; i++) {
      sym = sym + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(sym);
    }
  }

  rotate () {
    const inter = this.width;
    this.width = this.height;
    this.height = inter;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};
